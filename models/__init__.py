from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .role import Role
from .servicio import Servicio
from .reserva import Reserva
from .verification_token import VerificationToken
from .disponibilidad import Disponibilidad




