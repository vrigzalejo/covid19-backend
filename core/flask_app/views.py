from flask_app.schemas.base import schema
from flask_graphql import GraphQLView
from . import app

@app.route('/')
def root():
    return 'Covid19 Tracker GraphQL'


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
