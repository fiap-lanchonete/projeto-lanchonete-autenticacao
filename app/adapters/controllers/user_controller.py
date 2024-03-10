"""Module for user-related operations in the Flask application."""

from datetime import datetime, timedelta
from flask import current_app
from flask import Blueprint, request, jsonify
from pydantic import ValidationError

import jwt
from jwt.exceptions import InvalidTokenError

from ...application.dtos.create_user_dto import CreateUserDto

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/', methods=['POST'])
def create_user():
    """
    Creates a user in the database.
    
    Returns:
        A JSON response indicating the outcome of the create operation.
    """
    try:
        user_data = CreateUserDto(**request.json)

        user_repository = getattr(current_app, 'user_repository', None)

        if not user_repository:
            return jsonify({'error': 'Internal error'}), 500

        existing_user = user_repository.get_user_by_email(user_data.email)

        if existing_user:
            return jsonify({'error': 'User with this email already exists'}), 409

        user_repository.create_user(user_data.model_dump())

        return jsonify(user_data.model_dump()), 201
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {str(e)}")

        return jsonify({'error': 'An unexpected error occurred'}), 500

@user_blueprint.route('/', methods=['DELETE'])
def delete_user():
    """
    Deletes a user from the database based on the provided email.
    
    Returns:
        A JSON response indicating the outcome of the delete operation.
    """
    try:
        email = request.args.get('email')

        if not email:
            return jsonify({'error': 'Email is required'}), 400

        user_repository = getattr(current_app, 'user_repository', None)

        if not user_repository:
            return jsonify({'error': 'Internal error'}), 500

        user_repository.delete_by_email(email)

        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {str(e)}")

        return jsonify({'error': 'An unexpected error occurred'}), 500

@user_blueprint.route('/login', methods=['POST'])
def login():
    """
    Logs a user in.
    
    Returns:
        A JSON response indicating the outcome of the login operation.
    """
    try:
        payload = request.json
        cpf = payload.get('cpf')

        if not cpf:
            return jsonify({'error': 'CPF is required'}), 400

        user_repository = getattr(current_app, 'user_repository', None)
        if not user_repository:
            return jsonify({'error': 'Internal error'}), 500

        user = user_repository.get_user_by_cpf(cpf)

        if not user:
            return jsonify({'error': 'Wrong credentials'}), 401

        encoded_jwt = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=1)
        },  current_app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'message': 'Login successful', 'token': encoded_jwt }), 200
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {str(e)}")

        return jsonify({'error': 'An unexpected error occurred'}), 500

@user_blueprint.route('/verify_token', methods=['POST'])
def verify_token():
    """
    Verifies a token.
    
    Returns:
        A JSON response indicating the outcome of the token verification operation.
    """
    try:
        token = request.headers.get('Authorization')

        print(token)

        if not token:
            return jsonify({'error': 'Token is required'}), 400

        if token.startswith('Bearer '):
            token = token[7:]

        decoded_jwt = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=["HS256"],
        )

        user_repository = getattr(current_app, 'user_repository', None)
        if not user_repository:
            return jsonify({'error': 'Internal error'}), 500

        user = user_repository.get_user_by_id(decoded_jwt['user_id'])

        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({'message': 'Token verified successfully'}), 200
    except InvalidTokenError as error:
        current_app.logger.error(f"Invalid token: {str(error)}")

        return jsonify({'error': 'Invalid token'}), 401

    except Exception as error:
        current_app.logger.error(f"Unexpected error: {str(error)}")

        return jsonify({'error': 'An unexpected error occurred'}), 500
