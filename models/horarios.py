from . import db

class Horario(db.Model):
    __tablename__ = 'horarios'
    id = db.Column(db.Integer, primary_key=True)
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicios.id'), nullable=False)
    dia_semana = db.Column(db.String, nullable=False)
    hora_inicio = db.Column(db.String, nullable=False)
    hora_fin = db.Column(db.String, nullable=False)


