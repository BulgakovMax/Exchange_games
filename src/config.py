import os


class Config:
    DB_TYPE="postgres"
    DB_HOST="db"
    DB_PORT=5432
    DB_USER=os.environ.get("DB_USER")
    DB_PASSWORD=os.environ.get("DB_PASSWORD")
    DB_NAME=os.environ.get("DB_NAME")

    SQLALCHEMY_DATABASE_URI = f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'very_secret_key'

    # Flask-User settings
    USER_APP_NAME = "Flask-User QuickStart App"  # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False  # Disable email authentication
    USER_ENABLE_USERNAME = True  # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False  # Simplify register form


class DevConfig(Config):
    pass


class TestConfig(Config):
    pass


def run_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    elif env == "TEST":
        return TestConfig
    else:
        return Config
