"""Module for the user model in the database."""
from datetime import datetime
from .base import db

class User(db.Model):
    """
    Represents a user in the database.
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    cpf = db.Column(db.String(11), unique=True)
    email = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
