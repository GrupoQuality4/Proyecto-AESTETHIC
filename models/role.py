from . import db
from .roles_users import roles_users

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    permissions = db.Column(db.String(200), nullable=True)

    users = db.relationship('User', secondary=roles_users, back_populates='roles')



