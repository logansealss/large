from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .models import responses, claps

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

    posts = db.relationship("Post", back_populates="writer")
    responses = db.relationship("Post", secondary=responses, back_populates="responses")
    followers = db.relationship("User", secondary=follows, back_populates="followees")
    followees = db.relationship("User", secondary=follows, back_populates="followers")
    clappers = db.relationship("Post", secondary=claps, back_populates="clapped_posts")

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
            'about': self.about
        }
