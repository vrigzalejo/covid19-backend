from flask_app.schemas.base import schema
from flask_graphql import GraphQLView
from . import app
from flask_app.database.base import db
from flask_app import setup

@app.route('/')
def hello_world():
    # db.create_all()
    # setup.seed()
    return 'Hello From Graphql Tutorial!'


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
