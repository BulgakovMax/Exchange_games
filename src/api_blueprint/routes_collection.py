from flask import request
from flask_restful import Resource, marshal_with
from db import db
from models.models import CollectionModel, UserModel, GameModel
import json


class Collection(Resource):
    # method_decorators = [check_login]  # add decorator check_login to all methods from Main

    def get(self, value=None):
        if value:
            data = CollectionModel.query.get(value)
            return data
        return CollectionModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_post = CollectionModel(**data)
        db.session.add(new_post)
        db.session.commit()
        return "Successfully added a new news"

    def put(self, user_id, game_id):
        user = UserModel.query.get(user_id)
        game = GameModel.query.get(game_id)
        user.games.append(game)
        db.session.commit()
        return [user.name, game.title]

    def delete(self, user_id, game_id):
        user = UserModel.query.get(user_id)
        game = GameModel.query.get(game_id)
        user.games.delete(game)
        db.session.commit()
        return [user.name, game.title]
