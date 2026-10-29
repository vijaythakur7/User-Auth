from extensions import db
from models.user_model import User


def find_by_email(email):
    return User.query.filter_by(email=email).first()


def find_by_id(user_id):
    return db.session.get(User, int(user_id))


def create_user(name, email, password_hash):
    user = User(name=name, email=email, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()
    return user
