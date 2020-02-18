from flask import Blueprint, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, validators, FileField
from wtforms.validators import DataRequired
from utils import upload_image, parse_table, pars_automation

from db import db
from models.models import GameModel

game_bp = Blueprint('game',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/static/img/games_img'
                    )


class AddGameForm(FlaskForm):
    game_title = StringField('Title of game:', validators=[DataRequired()])
    game_alias = StringField('Alias of game:')
    rank_bgg = StringField('Rank BGG:')
    player_rate = FloatField('Player rate:', [validators.number_range(0, 10), validators.DataRequired()])
    bgg_rate = FloatField('BGG rate:', [validators.number_range(0, 10), validators.DataRequired()])
    player_min = IntegerField('Value of player minimum:', [validators.number_range(1, 20), validators.DataRequired()])
    player_max = IntegerField('Value of player maximum:', [validators.number_range(1, 20), validators.DataRequired()])
    language = StringField('Language of game:', validators=[DataRequired()])
    game_type = StringField('Type of game:')
    img_name = FileField()

    submit = SubmitField('Add game')


@game_bp.route('/games', methods=['GET'])
@game_bp.route('/games/<value>', methods=['GET'])
def get_game(value=None):
    games = GameModel.query.all()
    if value:
        game = GameModel.query.get(value)
        return render_template('game.html',
                               title='Game',
                               game=game
                               )
    return render_template('games.html',
                           title='List Of Games',
                           games=games,
                           )


@game_bp.route('/add_game', methods=['GET', 'POST'])
def add_game():
    form = AddGameForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = {
                'title': request.form.get('game_title'),
                'alias': request.form.get('game_alias'),
                "player_rate": request.form.get('player_rate'),
                "bgg_rate": request.form.get('bgg_rate'),
                "player_min": request.form.get('player_min'),
                "player_max": request.form.get('player_max'),
                "language": request.form.get('language'),
                "type": request.form.get('game_type'),
                'img_name': upload_image(request.files['img_name'])
            }
            new_post = GameModel(**data)
            db.session.add(new_post)
            db.session.commit()
            return redirect('/games')
    return render_template('add_game.html', form=form)


@game_bp.route('/pars_games', methods=['GET'])
def pars_games():
    bgg_games = pars_automation()
    for game in bgg_games:
        data = {
            'title': game.get('name'),
            'alias': game.get('name').replace(' ', '_').lower(),
            "rank_bgg": game.get('rank_bgg'),
            "player_rate": game.get('geek_rating'),
            "bgg_rate": game.get('geek_rating'),
            "link": game.get('link'),
            "avg_rating": game.get('avg_rating'),
            "num_voters": game.get('num_voters'),
            'img_name': game.get('image')
        }
        if not GameModel.query.filter_by(title=data.get('title')).first():
            new_game = GameModel(**data)
            db.session.add(new_game)
            db.session.commit()

    return redirect('/games')
