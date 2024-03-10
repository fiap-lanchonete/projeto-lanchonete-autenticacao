from ....adapters.database.models.user import User

class UserRepository:
    """Repository for user-related operations in the database."""

    def __init__(self, db):
        self.db = db

    def create_user(self, user):
        """Create a new user."""
        user_data = User(**user)

        self.db.session.add(user_data)
        self.db.session.commit()

        return user

    def get_user_by_email(self, email):
        """Get a user by email."""
        return self.db.session.query(User).filter_by(email=email).first()

    def get_user_by_cpf(self, cpf):
        """Get a user by CPF."""
        return self.db.session.query(User).filter_by(cpf=cpf).first()

    def get_user_by_id(self, user_id):
        """Get a user by ID."""
        return self.db.session.query(User).filter_by(id=user_id).first()

    def delete_by_email(self, email):
        """Delete a user by email."""
        self.db.session.query(User).filter_by(email=email).delete()
        self.db.session.commit()

        return True
