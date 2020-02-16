from flask import request
from flask_restful import Resource, marshal_with
from api_blueprint.marshal_structure import game_structure
from db import db
from models.models import GameModel
import json


class Game(Resource):
    # method_decorators = [check_login]  # add decorator check_login to all methods from Main

    @marshal_with(game_structure)
    def get(self, value=None):
        if value:
            data = GameModel.query.get(value)
            return data
        return GameModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_post = GameModel(**data)
        db.session.add(new_post)
        db.session.commit()
        return "Successfully added a new news"

    def put(self, value):
        data = json.loads(request.data)
        post = GameModel.query.get(value)

        post.title = data.get("title")
        post.text = data.get("text")

        db.session.commit()
        return "Successfully updated the value"

    def delete(self, value):
        post = GameModel.query.get(value)
        db.session.delete(post)
        db.session.commit()
        return "Successfully deleted the value"
