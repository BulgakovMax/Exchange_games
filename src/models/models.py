from db import db


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    games = db.relationship('GameModel', secondary='collection')


class CollectionModel(db.Model):
    __tablename__ = "collection"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    game = db.relationship('UserModel', backref='game_collection')
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
    img_name = db.Column(db.LargeBinary, nullable=True)
    users = db.relationship('UserModel', secondary='collection')

    def __repr__(self):
        return self.title
