from flask import Blueprint, render_template

wish_list_bp = Blueprint('wish list',
                         __name__,
                         template_folder='templates',
                         static_folder='static',
                         static_url_path='/products/static'
                         )


@wish_list_bp.route('/wish_list', methods=['GET'])
def get_wish_list():
    return render_template('wish_list.html',
                           title='Wish List'
                           )
