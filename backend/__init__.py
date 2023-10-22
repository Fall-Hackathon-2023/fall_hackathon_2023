from flask import Flask

from backend.routes.reviews import reviews_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(reviews_bp)

    return app
