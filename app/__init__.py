from flask import Flask

def create_app():
    app = Flask(__name__)

    from .user import bp_user
    app.register_blueprint(bp_user)

    return app