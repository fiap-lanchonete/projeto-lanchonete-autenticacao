from ....adapters.database.models.user import User

class UserRepository:
  def __init__(self, db):
    self.db = db

  def create_user(self, user):
    user_data = User(**user)

    self.db.session.add(user_data)
    self.db.session.commit()

    return user

  def get_user_by_email(self, email):
    return self.db.session.query(User).filter_by(email=email).first()
  
  def delete_by_email(self, email):
    self.db.session.query(User).filter_by(email=email).delete()
    self.db.session.commit()

    return True
