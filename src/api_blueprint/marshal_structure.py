from flask_restful import fields


game_structure = {
    "title": fields.String,
    "alias": fields.String,
    "player_rate": fields.Float,
    "bgg_rate": fields.Float,
    "player_min": fields.Integer,
    "player_max": fields.Integer,
    "language": fields.String,
    "type": fields.String,
    "img_name": fields.String
}

user_structure = {
    "name": fields.String,
    "email": fields.String,
    "games": fields.Nested(game_structure)
}

