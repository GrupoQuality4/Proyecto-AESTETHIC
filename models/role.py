from . import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    permissions = db.Column(db.String(200), nullable=True)

