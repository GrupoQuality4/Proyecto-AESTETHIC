from datetime import datetime
from . import db

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    servicio = db.Column(db.String(100), nullable=False)
    fecha_reserva = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_uso = db.Column(db.DateTime, nullable=True)
    def __init__(self, user_id, servicio, fecha_uso=None):
        self.user_id = user_id
        self.servicio = servicio
        self.fecha_uso = fecha_uso

