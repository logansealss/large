from .db import db
from datetime import datetime

responses = db.Table(
    "responses",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
    db.Column("response", db.String(255), nullable=False),
    db.Column("created_at", db.DateTime, default=datetime.now())
)

claps = db.Table(
    "claps",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
    db.Column("amount", db.Integer, nullable=False)
)

post_tags = db.Table(
    "post_tags",
    db.Model.metadata,
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
)

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
    responses = db.relationship("User", secondary=responses, back_populates="reponses")
    clapped_posts = db.relationship("User", secondary=responses, back_populates="clappers")
    tags = db.relationship("Tag", secondary=post_tags, back_populates="posts")

class Tags(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    posts = db.relationship("Post", secondary=post_tags, back_populates="tags")




    