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

    print (SQLALCHEMY_DATABASE_URI)


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
