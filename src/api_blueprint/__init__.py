from flask import Blueprint
from flask_restful import Api
from api_blueprint.routes_game import Game
from api_blueprint.routes_user import User
from api_blueprint.routes_collection import Collection
from api_blueprint.routes_db import CreateDB

blueprint = Blueprint("api_blueprint", __name__)
api_blueprint = Api(blueprint)

api_blueprint.add_resource(Collection, "/collection/<user_id>/<game_id>")
api_blueprint.add_resource(Game, "/game", "/game/<value>")
api_blueprint.add_resource(User, "/user", "/user/<value>")
api_blueprint.add_resource(CreateDB, "/create_db")