from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String())
    avatar_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    posts = db.relationship("Post",
                            backref = "user",
                            lazy = "dynamic")
    comments = db.relationship("Comment",
                                backref = "user",
                                lazy = "dynamic")
    liked = db.relationship("PostLike",
                            backref = "user", 
                            lazy = "dynamic")
    
    
    
    
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    post_title = db.Column(db.String)
    post_content = db.Column(db.Text)
    posted_at = db.Column(db.DateTime)
    upvotes = db.Column(db.Integer, default = 0)
    downvotes = db.Column(db.Integer, default = 0)
    post_by = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship("Comment", 
                                foreign_keys = "Comment.post_id", 
                                backref = "post", 
                                lazy = "dynamic")
     