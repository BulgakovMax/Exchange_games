from flask import Blueprint, render_template
from flask_user import login_required

base_bp = Blueprint('base',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/products/static'
                    )


@base_bp.route('/', methods=['GET'])
def index():
    return render_template('base.html',
                           title='Base'
                           )


@base_bp.route('/contact', methods=['GET'])
@login_required
def contact():
    return render_template('contact.html',
                           title='Contact'
                           )
