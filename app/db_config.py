import os

config_path = os.path.dirname(__file__)
global_uri = os.environ["DATABASE_URL"]
if global_uri.startswith("postgres://"):
    global_uri = global_uri.replace("postgres://", "postgresql://", 1)


app_db_uri = global_uri
data_db_uri = global_uri
stream_db_uri = global_uri
aggregate_db_uri = global_uri


SQLALCHEMY_DATABASE_URI = app_db_uri
SQLALCHEMY_BINDS = {
    "app": app_db_uri,
    "data": data_db_uri,
    "stream": stream_db_uri,
    "aggregate": aggregate_db_uri
}


def configure_database(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_BINDS"] = SQLALCHEMY_BINDS
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config["SQLALCHEMY_ECHO"] = True
