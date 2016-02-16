from flask import Flask
from flask.ext.login import LoginManager
from app.core.models import db

def create_app():
    """
    Initialize && create app
    """
    app = Flask(__name__)
    app.config.from_object('config')
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
    init_db(app)
    init_login(app)
    init_blueprint(app)

    return app

def init_db(app):
    """
    Initialize db
    """
    db.init_app(app)
    db.app = app

def init_login(app):
    """
    Initialize login
    """
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'manage.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.core.models import User
        return User.query.get(int(user_id))

def init_blueprint(app):
    """
    Initialize blueprint
    """
    from app.core.home import home
    app.register_blueprint(home)

    from app.core.page import page
    app.register_blueprint(page)

    # from app.core.category import category
    # app.register_blueprint(category)
    #
    # from app.core.post import post
    # app.register_blueprint(post)
    #
    # from app.core.tag import tag
    # app.register_blueprint(tag)
