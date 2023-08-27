from flask import Flask, url_for

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kajsaksj'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
