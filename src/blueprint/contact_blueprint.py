from flask import Blueprint, render_template

contact_bp = Blueprint('contact',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='/products/static'
                       )


@contact_bp.route('/contact', methods=['GET'])
def get_contact():
    return render_template('contact.html',
                           title='Contact'
                           )
