from flask import Blueprint, render_template

base_bp = Blueprint('base',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/products/static'
                    )


@base_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html',
                           title='Index'
                           )


@base_bp.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html',
                           title='Contact'
                           )
