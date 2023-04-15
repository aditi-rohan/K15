# __init__.py makes the KomuniQ file a python __package__
# everything inside here will run automatically
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '680WJKD ASDkldaswugioe4843'

    # import the relevant routes from views.py and auth.py
    from .views import views
    from .auth import auth

    # register the Blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
