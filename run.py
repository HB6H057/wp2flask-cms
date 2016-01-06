#!flask/bin/python
from flask.ext.script import Manager

from app import create_app

if __name__ == '__main__':
    app = create_app()
    manager = Manager(app)
    manager.run()
