from . import db

class Horarios(db.Model):
    __tablename__ = 'horarios'
    id = db.Column(db.Integer, primary_key=True)
    dia_semana = db.Column(db.String(10), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=False)

    
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicio.id'), nullable=False)