from flask import Flask
from flask_restplus import Api

from db import db
from config import Config
from controllers.entry import entries_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    db.init_app(app)

    @app.route('/')
    def index():
        return 'It works!'

    api = Api(app, doc='/docs/')
    api.add_namespace(entries_ns)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", debug=True)

