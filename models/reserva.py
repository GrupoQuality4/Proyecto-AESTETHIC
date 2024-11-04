from sqlalchemy.orm import relationship
from . import db

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    servicio = db.Column(db.String(50), nullable=False)
    fecha_reserva = db.Column(db.Date, nullable=False)
    fecha_uso = db.Column(db.Date, nullable=False)

    user = relationship("User", back_populates="reservas")

    def __init__(self, user_id, servicio, fecha_reserva, fecha_uso):
        self.user_id = user_id
        self.servicio = servicio
        self.fecha_reserva = fecha_reserva
        self.fecha_uso = fecha_uso

