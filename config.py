import os
import logging

from db import *

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'buyaoyongroot'
CSRF_ENABLE = True

# remove to db.py
# MYSQL_USERNAME = 'root'
# MYSQL_PASSWORD = '123123'
# MYSQL_HOST = 'localhost'
# MYSQL_DBNAME = 'flask'

LOGGING_PATH = os.path.join(basedir, 'logs')
LOGGING_FILENAME = 'wp2flask-cms.log'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (MYSQL_USERNAME,
                                                           MYSQL_PASSWORD,
                                                           MYSQL_HOST,
                                                           MYSQL_DBNAME)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

fh = logging.FileHandler('%s/%s' % (LOGGING_PATH, LOGGING_FILENAME))
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger = logging.getLogger('wp2flask-cms')
logger.setLevel(logging.DEBUG)

logger.addHandler(fh)
logger.addHandler(ch)
