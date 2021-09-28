from ImgRepo import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    tags = db.Column(db.String(30), nullable=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}'), '{self.tags}')"