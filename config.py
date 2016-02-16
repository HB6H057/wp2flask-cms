import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'buyaoyongroot'

MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '123123'
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'flask'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (MYSQL_USERNAME,
                                                           MYSQL_PASSWORD,
                                                           MYSQL_HOST,
                                                           MYSQL_DBNAME)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLE = True
