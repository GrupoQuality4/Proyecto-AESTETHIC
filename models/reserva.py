from datetime import datetime
from . import db

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicios.id'), nullable=False)
    fecha_reserva = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_uso = db.Column(db.DateTime, nullable=True)

    # Relaciones
    usuario = db.relationship('User', backref='reservas', lazy=True)
    servicio = db.relationship('Servicio', backref='reservas', lazy=True)
