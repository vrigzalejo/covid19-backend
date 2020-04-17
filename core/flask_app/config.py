import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'database/covid19.sqlite3'
    )
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'database/covid19.sqlite3'
    )
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False
