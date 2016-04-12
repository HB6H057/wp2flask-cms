# encoding: utf-8
from app.core.models import db
from config import logger


def try_curd(fn):
    def wrapped(*args, **kwargs):
        try:
            fn(*args, **kwargs)
            logger.debug('test curd')
        except Exception, e:
            logger.error('Service curd error: %s' % e)
            db.session.rollback()
        else:
            logger.info('Service curd success: %s' % str(args))
            db.session.commit()
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

    # @try_curd
    # def add_all(self, objs):
    #     db.session.add_all(objs)

    @try_curd
    def delete(self, obj):
        if isinstance(obj, int):
            obj = self.model.query.get(obj)
            db.session.delete(obj)
        elif isinstance(obj, (db.Model)):
            db.session.delete(obj)
        elif isinstance(obj, list):
            self.__delete(list)
        else:
            assert TypeError, "obj must be int/Model/list, not %s" % type(obj)

    def __delete(self, list):
        ms = self.model.query.all()
        for m in ms:
            db.session.delete(m)

    # def delete_all(self, list):
    #     ms = self.model.query.all()
    #     self.__delete(ms)

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
