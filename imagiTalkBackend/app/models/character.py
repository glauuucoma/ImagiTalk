from app import db
from datetime import datetime

# ========== CHARACTER MODEL ==========
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(255))
    character_picture = db.Column(db.String(255))

    def __init__(self, character_name, character_picture):
        self.character_name = character_name
        self.character_picture = character_picture
        self.profile_picture = profile_picture