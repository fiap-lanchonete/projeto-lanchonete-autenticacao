"""Module for the Flask application."""

import atexit
import os
from flask import Flask

from .adapters.events.rabbit_mq.rabbit_mq_event_repository import RabbitMqEventRepository

from .adapters.controllers import user_controller
from .adapters.database.repositories.user_repository import UserRepository
from .adapters.database.models.base import Base, db
from .adapters.database.models.user import User

def create_app():
    """Create a new Flask application."""
    app = Flask(__name__)
    app.config.from_pyfile('settings.py', silent=False)

    print(app.config)

    app.register_blueprint(
        user_controller.user_blueprint,
        url_prefix='/user'
    )

    db.init_app(app)

    with app.app_context():
        db.create_all()

    setattr(app, 'db', db)

    user_repository = UserRepository(db)
    rabbit_mq_event_repository = RabbitMqEventRepository(app)

    setattr(app, 'user_repository', user_repository)
    setattr(app, 'rabbit_mq_event_repository', rabbit_mq_event_repository)

    atexit.register(rabbit_mq_event_repository.close_connection)

    return app
