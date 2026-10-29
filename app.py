from flask import Flask
from config import Config
from extensions import db, jwt

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/users")

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)