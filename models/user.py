from . import db
from .roles_users import roles_users
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    reservas = relationship("Reserva", back_populates="user")
    roles = db.relationship('Role', secondary=roles_users, back_populates='users')
    verification_tokens = relationship("VerificationToken", back_populates="user")






