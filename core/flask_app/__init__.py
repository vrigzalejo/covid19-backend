import os

from flask import Flask

app = Flask(__name__)

configurations = {
    "production": "flask_app.config.ProductionConfig",
    "development": "flask_app.config.DefaultConfig",
}

__env = os.getenv("FLASK_ENV", "development")
app.config.from_object(configurations[__env])

import flask_app.database.base  # noqa: E402
import flask_app.views  # noqa: E402, F401
