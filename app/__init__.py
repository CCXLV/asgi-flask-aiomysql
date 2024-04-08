from flask import Flask

from app.commands import init_db
from app.views.routes import routes_blueprint

def create_app():
    app = Flask(__name__)

    app.cli.add_command(init_db)
    app.register_blueprint(routes_blueprint)

    return app