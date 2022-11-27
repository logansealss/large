from .db import db
from sqlalchemy import select, func
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

post_tags = db.Table(
    "post_tags",
    db.Model.metadata,
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
)

follows = db.Table(
    "follows",
    db.Model.metadata,
    db.Column("follower_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("followee_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    about = db.Column(db.String(200))
    image_url = db.Column(db.String(255))

    posts = db.relationship("Post", back_populates="writer", cascade="all, delete-orphan")
    responses = db.relationship("Response", back_populates="user", cascade="all, delete-orphan")
    claps = db.relationship("Clap", back_populates="user", cascade="all, delete-orphan")
    following = db.relationship(
        "User",
        secondary=follows,
        primaryjoin=id == follows.c.follower_id,
        secondaryjoin=id == follows.c.followee_id,
        backref="followers"
    )
    
    follower_count = db.column_property(
        select(func.count(follows.c.followee_id))\
        .where(follows.c.followee_id == id)\
        .correlate_except(follows)\
        .scalar_subquery()\
    )

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'about': self.about,
            'imageURL': self.image_url,
            'followerCount': self.follower_count
        }

    def to_dict_with_followers(self):
                return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'about': self.about,
            'imageURL': self.image_url,
            'followerCount': self.follower_count,
            'followers': self.followers
        }

class Response(db.Model):
    __tablename__ = 'responses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    response = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    post = db.relationship("Post", back_populates="responses")
    user = db.relationship("User", back_populates="responses")

    def to_dict(self):
        return {
            "id": self.id,
            "response": self.response,
            "createdAt": self.created_at,
            "userId": self.user_id,
            "postId": self.post_id
        }

    def to_dict_with_user(self):
        return {
            "id": self.id,
            "response": self.response,
            "createdAt": self.created_at,
            "user": self.user.to_dict(),
            "postId": self.post_id
        }

class Clap(db.Model):
    __tablename__ = 'claps'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    post = db.relationship("Post", back_populates="claps")
    user = db.relationship("User", back_populates="claps")

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "userId": self.user_id,
            "postId": self.post_id
        }

    def to_dict_with_user(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "postId": self.post_id,
            "user": self.user.to_dict()
        }


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    writer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(100))
    read_time = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))
    post = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    writer = db.relationship("User", back_populates="posts")
    responses = db.relationship("Response", back_populates="post", cascade="all, delete-orphan")
    claps = db.relationship("Clap", back_populates="post", cascade="all, delete-orphan")
    tags = db.relationship("Tag", secondary=post_tags, back_populates="posts")

    def to_dict(self):
        return {
            "id": self.id,
            "writer": self.writer.to_dict(),
            "title": self.title,
            "subtitle": self.subtitle or None,
            "post": self.post,
            "readTime": self.read_time,
            "imageURL": self.image_url or None,
            "createdAt": self.created_at
        }

    def preview_to_dict(self):
        return {
            "id": self.id,
            "writer": self.writer.to_dict(),
            "title": self.title,
            "preview": self.subtitle or self.post[0:100],
            "readTime": self.read_time,
            "imageURL": self.image_url or None,
            "createdAt": self.created_at
        }

    def writer_to_dict(self):
        return {
            "id": self.id,
            "writerId": self.writer_id,
            "title": self.title,
            "preview": self.subtitle or self.post[0:100],
            "readTime": self.read_time,
            "imageURL": self.image_url or None,
            "createdAt": self.created_at
        }

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    posts = db.relationship("Post", secondary=post_tags, back_populates="tags")




    