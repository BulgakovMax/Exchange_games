from flask import Blueprint, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from db import db
from models.models import UserModel, GameModel

user_bp = Blueprint('user',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/products/static'
                    )


class SelectGame(FlaskForm):

    game = QuerySelectField('Select game', query_factory=lambda: GameModel.query.all())
    submit = SubmitField('Add game')


class AddUserForm(FlaskForm):
    user_name = StringField('Name of user:', validators=[DataRequired()])
    user_email = StringField('Email of user:', validators=[DataRequired()])
    submit = SubmitField('Add user')


@user_bp.route('/users', methods=['GET'])
@user_bp.route('/users/<value>', methods=['GET', 'POST'])
def user(value=None):
    users = UserModel.query.all()
    if value:
        user = UserModel.query.get(value)
        select_game_form = SelectGame()
        games = user.games
        if request.method == 'POST':
            if select_game_form.validate_on_submit():
                game_id = request.form.get('game')
                game = GameModel.query.get(game_id)
                user.games.append(game)
                db.session.commit()
                return redirect(f'/users/{value}')
        return render_template('user.html',
                               title='User',
                               user=user,
                               games=games,
                               form=select_game_form
                               )
    return render_template('users.html',
                           title='Users',
                           users=users,
                           )


@user_bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = AddUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = {
                'name': request.form.get('user_name'),
                'email': request.form.get('user_email')
            }
            new_post = UserModel(**data)
            db.session.add(new_post)
            db.session.commit()
            return redirect('/users')
    return render_template('add_user.html', form=form)
