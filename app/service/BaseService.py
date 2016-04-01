# encoding: utf-8
from app.core.models import db


def try_curd(fn):
    def wrapped(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except:
            print '-----------------test---------------------'
            db.session.rollback()
    return wrapped


class BaseService(object):
    def __init__(self, model=None):
        self.model = model

    def get(self, id):
        return self.model.query.get(id)

    def get_list(self):
        pass

    @try_curd
    def add(self, obj):
        db.session.add(obj)
        self.save()

    @try_curd
    def add_all(self, objs):
        db.session.add_all(objs)
        self.save()

    @try_curd
    def delete(self, id):
        db.session.delete(obj)
        self.save()

    @try_curd
    def delete_all(self):
        ms = self.model.query.all()
        for m in ms:
            db.session.delete(m)
        self.sava()

    def save(self):
        db.session.commit()


class CategoryService(BaseService):
    pass


class PostService(BaseService):
    pass


class TagService(BaseService):
    pass


class CommentService(BaseService):
    pass
