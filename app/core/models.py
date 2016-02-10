import re
from datetime import datetime

from xpinyin import Pinyin

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

post_tag_table = db.Table(
    'post_tag',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
)

class BaseModels(object):
    def toslug(self, name):
        '''
            1. chinese to pinyin.
            2. to lower.
            3. remove special character. (except: '-',' ')
            4. to convert ' ' into '-'
            5. fix special case of slug.
                I.  multi '-', eg: 'GlaDOS's block' ---> 'gladoss--blog'
                II. ...
        '''
        name = Pinyin().get_pinyin(name)
        pattern = re.compile(r'[^a-zA-z0-9\-]')
        slug = re.sub(pattern, '', name.lower().replace(' ', '-'))
        slug = re.sub('-+', '-', slug)
        return slug

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    nickname = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    posts = db.relationship('Post', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('error: password onlyread')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %s>' % self.username

class Category(db.Model, BaseModels):
    id = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(64), index=True, unique=True)
    slug = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(128))

    posts = db.relationship('Post', backref='category', lazy='dynamic')

    @property
    def name(self):
        return self.name_

    @name.setter
    def name(self, name):
        self.name_ = name
        self.slug = self.toslug(name)

    def __repr__(self):
        return '<Category %s>' % self.name

class Post(db.Model, BaseModels):
    id = db.Column(db.Integer, primary_key=True)
    title_ = db.Column(db.String(128), index=True, unique=True)
    slug = db.Column(db.String(128), index=True, unique=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    tags = db.relationship('Tag', secondary=post_tag_table,
                            backref=db.backref('posts', lazy='dynamic')
                          )

    @property
    def title(self):
        return self.title_

    @title.setter
    def title(self, title):
        self.title_ = title
        self.slug = self.toslug(title)

    def __repr__(self):
        return '<Post %s>' % self.title

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    site = db.Column(db.String(64))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

class Tag(db.Model, BaseModels):
    id = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(64), index=True, unique=True)
    slug = db.Column(db.String(64), index=True, unique=True)

    # posts m2m

    @property
    def name(self):
        return self.name_

    @name.setter
    def name(self, name):
        self.name_ = name
        self.slug = self.toslug(name)

    def __repr__(self):
        return '<Tag %s>' % self.name
