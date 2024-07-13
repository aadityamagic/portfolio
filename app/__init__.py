from flask import Flask
from flask_assets import Environment, Bundle

def create_app():
    app = Flask(__name__)
    assets = Environment(app)

    scss = Bundle('modern.scss', filters='libsass', output='modern.css')
    print("here",scss)
    assets.register('scss_all', scss)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes

        return app
