from flask import request, make_response, render_template
from flask_restful import Resource, marshal_with
from api_blueprint.marshal_structure import user_structure
from db import db
from models.models import User
import json


class User(Resource):
    # method_decorators = [check_login]  # add decorator check_login to all methods from Main

    @marshal_with(user_structure)
    def get(self, value=None):
        if value:
            data = User.query.get(value)
            return data
        return User.query.all()

    def post(self):
        data = json.loads(request.data)
        print(data)
        new_post = User(**data)
        db.session.add(new_post)
        db.session.commit()
        return "Successfully added a new news"

    def put(self, value):
        data = json.loads(request.data)
        post = User.query.get(value)

        post.title = data.get("title")
        post.text = data.get("text")

        db.session.commit()
        return "Successfully updated the value"

    def delete(self, value):
        post = User.query.get(value)
        db.session.delete(post)
        db.session.commit()
        return "Successfully deleted the value"
