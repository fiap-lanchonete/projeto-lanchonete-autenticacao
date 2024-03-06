from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(DeclarativeBase):
  pass
