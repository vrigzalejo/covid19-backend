import os

from flask import Flask

app = Flask(__name__)

configurations = {
    "production": "flask_app.config.DefaultConfig",
    "development": "flask_app.config.DefaultConfig",
}

app.config.from_object(configurations[os.getenv("FLASK_ENV")])

import flask_app.database.base
import flask_app.views
