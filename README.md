# User Service - Flask Microservices

This is the first standalone microservice extracted from the JWT Login project.

## Responsibility
- User registration
- User login
- JWT authentication
- User profile

## Architecture
Request -> Controller -> Service -> Repository -> Model -> Database

## Structure
controllers/auth_controller.py
services/auth_service.py
repositories/user_repository.py
models/user_model.py

## Endpoints
POST /api/users/register
POST /api/users/login
GET /api/users/profile

## Run
python app.py

The existing business logic, validation, password hashing and JWT behavior are preserved. The main microservice change is that this application now has a clearly defined User Service boundary.
