from flask import Flask

from backend.routes.reviews import reviews_bp
from backend.routes.reviews import populate_db


def create_app():
    app = Flask(__name__)

    app.register_blueprint(reviews_bp)

    populate_db()

    return app
