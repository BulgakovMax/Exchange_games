from datetime import timedelta

from flask import Flask
from blueprint.user_blueprint import user_bp
from blueprint.game_blueprint import game_bp
from blueprint.base_blueprint import base_bp
from blueprint.wish_list_blueprint import wish_list_bp
from config import run_config
from api_blueprint import blueprint
from db import db
from flask_migrate import Migrate
from flask_user import UserManager
from models.models import User


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config.from_object(run_config())

    db.init_app(app)
    migrate = Migrate(app, db)
    app.permanent_session_lifetime = timedelta(minutes=20)  # add session expire time
    UserManager(app, db, User)
    app.register_blueprint(blueprint, url_prefix='/api')
    app.register_blueprint(user_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(base_bp)
    app.register_blueprint(wish_list_bp)

    return app


if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=8000, debug=True)
