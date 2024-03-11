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
        credentials = pika.PlainCredentials(
            username=app.config['RABBITMQ_USER'],
            password=app.config['RABBITMQ_PASSWORD']
        )

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=app.config['RABBITMQ_HOST'],
                port=app.config['RABBITMQ_PORT'],
                credentials=credentials
            )
        )

        self.setup_exchange(app)

    def setup_exchange(self, app):
        """
        Sets up the exchange on the RabbitMQ broker.
        """
        channel = self.connection.channel()

        self.exchange_name = app.config['RABBITMQ_EXCHANGE_NAME']
        self.routing_key = app.config['RABBITMQ_ROUTING_KEY']

        channel.exchange_declare(
            exchange=self.exchange_name,
            exchange_type='topic',
            durable=True
        )

    def publish_event(self, event_data: dict):
        """
        Publishes an event to the RabbitMQ broker.
        """
        channel = self.connection.channel()
        channel.queue_declare(queue=current_app.config['RABBITMQ_QUEUE_NAME'])

        channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=json.dumps(event_data),
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )

        if current_app.config['DEBUG']:
            print(f"sent to exchange {self.exchange_name} with data: {event_data}")

        self.connection.close()
