from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from repositories import user_repository


def register(data):
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    if not name or not email or not password:
        return {"message": "All fields are required"}, 400
    existing_user = user_repository.find_by_email(email)
    if existing_user:
        return {"message": "User already exists"}, 409
    password_hash = generate_password_hash(password)
    user_repository.create_user(name, email, password_hash)
    return {"message": "User registered successfully"}, 201


def login(data):
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return {"message": "Email and password are required"}, 400
    user = user_repository.find_by_email(email)
    if not user:
        return {"message": "Invalid email or password"}, 401
    if not check_password_hash(user.password_hash, password):
        return {"message": "Invalid email or password"}, 401
    access_token = create_access_token(identity=str(user.id))
    return {"message": "Login successful", "access_token": access_token}, 200


def profile(user_id):
    user = user_repository.find_by_id(user_id)
    if not user:
        return {"message": "User not found"}, 404
    return {"id": user.id, "name": user.name, "email": user.email}, 200
