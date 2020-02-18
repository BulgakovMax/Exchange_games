from db import db
from flask_user import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=True, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean()),
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)

    games = db.relationship('GameModel', secondary='collection')


class CollectionModel(db.Model):
    __tablename__ = "collection"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    game = db.relationship('User', backref='game_collection')
    user = db.relationship('GameModel', backref='user_collection')


class GameModel(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    alias = db.Column(db.String(128), nullable=False)
    player_rate = db.Column(db.Float, nullable=False)
    bgg_rate = db.Column(db.Float, nullable=False)
    player_min = db.Column(db.Integer, nullable=False)
    player_max = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(128), nullable=True)
    type = db.Column(db.String(128), nullable=True)
    img_name = db.Column(db.String(128), nullable=True)
    users = db.relationship('User', secondary='collection')

    def __repr__(self):
        return self.title
