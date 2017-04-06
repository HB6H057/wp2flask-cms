from flask import Flask

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
    init_restful(app)
    init_admin(app)
    init_babel(app)

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
    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'manage.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.core.models import User
        return User.query.get(int(user_id))


def init_blueprint(flask_app):
    """
    Initialize blueprint
    """
    from app.core.home import home
    flask_app.register_blueprint(home)

    from app.core.page import page
    flask_app.register_blueprint(page)

    from app.core.module import module
    flask_app.register_blueprint(module)

    # from app.core.apiv1 import apiv1
    # app.register_blueprint(apiv1, url_prefix='/api/v1')


def init_restful(flask_app):
    from app.core.apiv1 import apiv1
    apiv1.init_app(flask_app)
    apiv1.app = flask_app


def init_admin(flask_app):
    from flask_admin import Admin

    admin = Admin(flask_app, name='manager', template_mode='bootstrap3')

    from core.admin.views import MyView, PostView, CategoryView, TagView

    admin.add_view(MyView(name='test', endpoint='test'))
    admin.add_view(PostView(db.session))
    admin.add_view(CategoryView(db.session))
    admin.add_view(TagView(db.session))

    return admin


def init_babel(flask_app):
    from flask_babelex import Babel
    babel = Babel(flask_app)
    flask_app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
    return babel
