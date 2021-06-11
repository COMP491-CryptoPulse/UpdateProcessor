from flask import Flask
from flask_cors import CORS

from data.database import db
from app.db_config import configure_database
from app.blueprints import update_blueprint

NPM_OUT = "../web/out"


def create_app():
    app = Flask(__name__)
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    CORS(app)
    configure_database(app)
    app.register_blueprint(update_blueprint, url_prefix="/update")

    # Initialize the database.
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


app = create_app()
