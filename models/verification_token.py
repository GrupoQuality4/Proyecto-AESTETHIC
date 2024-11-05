from . import db
from sqlalchemy.orm import relationship

class VerificationToken(db.Model):
    __tablename__ = 'verification_token'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="verification_tokens")


