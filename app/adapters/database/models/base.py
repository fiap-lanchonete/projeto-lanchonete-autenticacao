from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(DeclarativeBase):
    """
    Represents a base model in the database.
    """
    __abstract__ = True
