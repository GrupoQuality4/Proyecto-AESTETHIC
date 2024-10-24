from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .servicio import Servicio
from .user import User
from .role import Role
from .roles_users import roles_users
from .verification_token import VerificationToken
from .servicio import Servicio
