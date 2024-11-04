from sqlalchemy.orm import relationship
from . import db

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
<<<<<<< HEAD
    servicio = db.Column(db.String(50), nullable=False)
    fecha_reserva = db.Column(db.Date, nullable=False)
    fecha_uso = db.Column(db.Date, nullable=False)
=======
    nombre_cliente = db.Column(db.String(50), nullable=False)
    servicio = db.Column(db.String(50), nullable=False)
    fecha_reserva = db.Column(db.Date, nullable=False)
    fecha_uso = db.Column(db.Date, nullable=False)
    horario = db.Column(db.String(20), nullable=True)
>>>>>>> 1a11c122b901de224348ce0ba795a7c22741fa39

    user = relationship("User", back_populates="reservas")

    def __init__(self, user_id, servicio, fecha_reserva, fecha_uso):
        self.user_id = user_id
        self.servicio = servicio
        self.fecha_reserva = fecha_reserva
        self.fecha_uso = fecha_uso

