import os
from functools import wraps

from flask import session


def check_login(f):
    """
    This decorator will check your logged_in parameter from session
    if it false you will see msg "You must login to see this page"
    if it true you will see the content of your page

    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get("logged_in"):
            func = f(*args, **kwargs)
        else:
            return "You must login to see this page"
        return func

    return wrapper


def upload_image(request_files):
    if request_files:
        image = request_files
        image.save(os.path.join('/static/img/games_img', image.filename))
        return image.filename
    else:
        return 'no_image.jpg'
