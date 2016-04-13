# encoding: utf-8
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from app.core.models import *
from config import logger


def try_read(fn):
    def wrapped(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except NoResultFound, e:
            logger.info(' No Query Result Found: %s' % str(kwargs))
        except MultipleResultsFound, e:
            logger.error('Multiple Query Results Found: %s' % str(kwargs))
        except Exception, e:
            logger.error('Query Error: %s' % e)
    return wrapped


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

    def get(self, **kwargs):
        logger.debug('slef.get: %s' % str(kwargs))
        model = self.model.query.filter_by(**kwargs).one()
        return model

    def get_list(self, limit=None, offset=None, **kwargs):
        models = self.model.query.filter_by(**kwargs).limit(limit).\
                                                      offset(offset).all()
        return models

    @try_curd
    def add(self, obj):
        db.session.add(obj)

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
            raise TypeError("obj must be int/Model/list, not %s" % type(obj))

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
    def __init__(self):
        super(CategoryService, self).__init__(model=Category)

    def get_cate_posts_by_id(self, cid):
        cate = self.get(id=cid)
        ps = cate.posts
        return ps


class PostService(BaseService):
    def __init__(self):
        super(PostService, self).__init__(model=Post)

    def get_post_tags_by_id(self, pid):
        post = self.get(id=pid)
        tags = post.tags

        return tags

    def get_post_cate_by_id(self, pid):
        post = self.get(id=pid)
        cate = post.category

        return cate

    def get_post_comments_by_id(self, pid):
        post = self.get(id=pid)
        cate = post.comments

        return cate


class TagService(BaseService):

    def __init__(self):
        super(TagService, self).__init__(model=Tag)

    def get_tag_posts_by_id(self, tid):
        tag = self.model.get(id=tid)
        ps = tag.posts

        return ps


class CommentService(BaseService):
    def __init__(self):
        super(CommentService, self).__init__(model=Comment)

    def get_comment_post_by_id(self, comid):
        comment = self.model.get(id=comid)
        post = comment.post

        return post
