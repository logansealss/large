from .db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# responses = db.Table(
#     "responses",
#     db.Model.metadata,
#     db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
#     db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
#     db.Column("response", db.String(255), nullable=False),
#     db.Column("created_at", db.DateTime, default=datetime.now())
# )

# claps = db.Table(
#     "claps",
#     db.Model.metadata,
#     db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
#     db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
#     db.Column("amount", db.Integer, nullable=False)
# )

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

    posts = db.relationship("Post", back_populates="writer", cascade="all, delete-orphan")
    responses = db.relationship("Response", back_populates="user")
    claps = db.relationship("Clap", back_populates="user")
    following = db.relationship(
        "User",
        secondary=follows,
        primaryjoin=id == follows.c.follower_id,
        secondaryjoin=id == follows.c.followee_id,
        backref="followers"
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
            'following': self.following,
            'followers': self.followers
        }

class Response(db.Model):
    __tablename__ = 'responses'

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)
    response = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    post = db.relationship("Post", back_populates="responses")
    user = db.relationship("User", back_populates="responses")



class Clap(db.Model):
    __tablename__ = 'claps'

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)
    amount = db.Column(db.Integer, nullable=False)

    post = db.relationship("Post", back_populates="claps")
    user = db.relationship("User", back_populates="claps")


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    writer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(100))
    read_time = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))
    post = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.now())

    writer = db.relationship("User", back_populates="posts")
    responses = db.relationship("Response", back_populates="post")
    claps = db.relationship("Clap", back_populates="post")
    tags = db.relationship("Tag", secondary=post_tags, back_populates="posts")

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    posts = db.relationship("Post", secondary=post_tags, back_populates="tags")




    