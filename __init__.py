from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import session

from .adapters.controllers import user_controller
from .adapters.database.repositories.user_repository import UserRepository
from .adapters.database.models.base import Base, db
from .adapters.database.models.user import User

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)

    if config_filename is not None:
      app.config.from_pyfile(config_filename)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['DEBUG'] = True

    app.register_blueprint(
      user_controller.user_blueprint,
      url_prefix='/user'
    )

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.db = db

    user_repository = UserRepository(db)
    app.user_repository = user_repository

    return app
