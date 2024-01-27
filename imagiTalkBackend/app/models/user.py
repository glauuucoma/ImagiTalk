from app import db
from datetime import datetime

# ========== USER MODEL ==========
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auth0_id = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
    updated_at = db.Column(db.String(255))

    def __init__(self, username, email, profile_picture, updated_at):
        self.username = username
        self.email = email
        self.profile_picture = profile_picture
        self.updated_at = updated_at