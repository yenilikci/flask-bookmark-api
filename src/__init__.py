from flask import Flask, jsonify
import os
from src.auth import auth
from src.bookmarks import bookmarks


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY")
        )
    else:
        app.config.from_mapping(test_config)

    @app.get("/")
    def index():
        return 'hello world'

    @app.get("/hello")
    def sayHello():
        return jsonify({'message': 'hello world'})

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

    return app
