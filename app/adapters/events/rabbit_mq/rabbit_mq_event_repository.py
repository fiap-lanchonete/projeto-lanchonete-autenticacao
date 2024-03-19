"""
This module contains the RabbitMQ event repository.
"""

import json
import pika

from flask import current_app

class RabbitMqEventRepository:
    """
    This class is responsible for publishing events to the RabbitMQ broker.
    """
    def __init__(self, app):
        self.url_string = f"amqps://{app.config['RABBITMQ_USER']}:{app.config['RABBITMQ_PASSWORD']}@{app.config['RABBITMQ_HOST']}:{app.config['RABBITMQ_PORT']}/?heartbeat=0"
        self.url_parameter = pika.URLParameters(self.url_string)
        self.connection = pika.BlockingConnection(
            self.url_parameter
        )

        self.routing_key = app.config['RABBITMQ_ROUTING_KEY']

    def publish_event(self, event_data: dict):
        """
        Publishes an event to the RabbitMQ broker.
        """
        channel = self.connection.channel()
        channel.queue_declare(
            queue=current_app.config['RABBITMQ_QUEUE_NAME'],
            durable=True
        )

        channel.basic_publish(
            exchange='',
            routing_key=current_app.config['RABBITMQ_ROUTING_KEY'],
            body=json.dumps(event_data),
        )

        if current_app.config['DEBUG']:
            print(f"sent to exchange with data: {event_data}")

    def close_connection(self):
        """
        Closes the RabbitMQ connection.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            print('RabbitMQ connection closed.')
