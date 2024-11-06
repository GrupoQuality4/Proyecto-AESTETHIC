from . import db
from sqlalchemy.orm import relationship

class VerificationToken(db.Model):
    __tablename__ = 'verification_tokens'
    
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    is_used = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    user = db.relationship("User", back_populates="verification_tokens")





