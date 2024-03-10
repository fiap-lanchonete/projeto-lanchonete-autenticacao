"""Module for the Flask application."""

from flask import Flask

from .adapters.controllers import user_controller
from .adapters.database.repositories.user_repository import UserRepository
from .adapters.database.models.base import Base, db
from .adapters.database.models.user import User

def create_app(config_filename=None):
    """Create a new Flask application."""
    app = Flask(__name__)

    if config_filename is not None:
        app.config.from_pyfile(config_filename, silent=False)

    app.register_blueprint(
        user_controller.user_blueprint,
        url_prefix='/user'
    )

    db.init_app(app)

    with app.app_context():
        db.create_all()

    setattr(app, 'db', db)

    user_repository = UserRepository(db)
    setattr(app, 'user_repository', user_repository)

    return app
