# encoding: utf-8
from datetime import datetime

from slugify import slugify

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

post_tag_table = db.Table(
    'post_tag',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
)


class PageModelMixin(db.Model):
    __abstract__ = True

    create_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, index=True, default=datetime.utcnow, onupdate=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if 'slug' not in kwargs:
            kwargs['slug'] = self.make_slug()
        super(PageModelMixin, self).__init__(*args, **kwargs)

    def get_slug_field(self):
        raise NotImplementedError

    def make_slug(self):
        field = self.get_slug_field()
        slug_ = slugify(field)
        model = self.__class__
        if slug_ is None:
            raise TypeError('%s slugify Error' % model)

        # TODO: 优化
        i = 2
        while model.query.filter_by(slug=slug_).first() is not None:
            slug_ = "%s-%s" % (slug_, i)
            i += 1

        return slug_


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    nickname = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    posts = db.relationship('Post', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('error: password only read')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %s>' % self.username


class Category(PageModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    slug = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(128))

    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def get_slug_field(self):
        return self.name

    def __repr__(self):
        return '<Category %s>' % self.name


class Post(PageModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    slug = db.Column(db.String(128), index=True, unique=True)
    body = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    tags = db.relationship(
        'Tag',
        secondary=post_tag_table,
        backref=db.backref('posts', lazy='dynamic')
    )

    def get_slug_field(self):
        return self.title

    def __repr__(self):
        return '<Post %s>' % self.title


class Tag(PageModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    slug = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(128))

    # posts m2m

    def get_slug_field(self):
        return self.name

    def __repr__(self):
        return '<Tag %s>' % self.name


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    site = db.Column(db.String(64))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, index=True, default=datetime.utcnow, onupdate=datetime.utcnow())

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return '<Comment %s>' % self.content
