from flask import Blueprint, request, jsonify
from flask import current_app
from pydantic import ValidationError

from ...application.dtos.create_user_dto import CreateUserDto

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/', methods=['POST'])
def create_user():
    try:
        user_data = CreateUserDto(**request.json)

        existing_user = current_app.user_repository.get_user_by_email(user_data.email)

        if existing_user:
            return jsonify({'error': 'User with this email already exists'}), 409

        user_repository = current_app.user_repository
        user_repository.create_user(user_data.model_dump())

        return jsonify(user_data), 201
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {str(e)}")

        return jsonify({'error': 'An unexpected error occurred'}), 500

@user_blueprint.route('/', methods=['DELETE'])
def delete_user():
    try:
        email = request.args.get('email')

        if not email:
            return jsonify({'error': 'Email is required'}), 400

        user_repository = current_app.user_repository
        user_repository.delete_by_email(email)

        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {str(e)}")

        return jsonify({'error': 'An unexpected error occurred'}), 500
