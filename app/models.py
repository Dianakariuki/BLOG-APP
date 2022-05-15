from . import db
from flask_login import UserMixin
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from . import login_manager

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


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
    
    

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    
    
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
     