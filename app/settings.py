"""Module for application settings."""
from os import environ

SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
SECRET_KEY = environ.get('SECRET_KEY')

RABBITMQ_HOST = environ.get('RABBITMQ_HOST')
RABBITMQ_USER = environ.get('RABBITMQ_USER')
RABBITMQ_PASSWORD = environ.get('RABBITMQ_PASSWORD')
RABBITMQ_PORT = environ.get('RABBITMQ_PORT')
RABBITMQ_EXCHANGE_NAME = environ.get('RABBITMQ_EXCHANGE_NAME')
RABBITMQ_ROUTING_KEY = environ.get('RABBITMQ_ROUTING_KEY')
RABBITMQ_QUEUE_NAME = environ.get('RABBITMQ_QUEUE_NAME')
RABBITMQ_HEARTBEAT = environ.get('RABBITMQ_HEARTBEAT')
