# encoding: utf-8
from app.core.base import *

from . import home

class HomeSerive(BaseSerive):
    @classmethod
    def get_index_data(cls):
        # get hot_list
        hot_list = cls.random_get_data(model=Post, count=11)
        # get brief
        new_post = Post.query.limit(3).all()
        # get categorys
        categorys = Category.query.all()
        # get cate_list
        cate_list = []
        for c in categorys:
            cate_posts = c.posts[:5]
            cate_list.append(cate_post_list)

        return fix_index_data(origin_data)

    def fix_index_data(cls, origin_data):
        origin_data['hot_list']

        data = dict(
            hot_list = [
                dict(title=p['title'], cate_slug=p['cate_slug'], slug=p['slug'])
                for p in hot_list
            ],

            new_post = [
                dict(title=p['title'], brief=p['body'],
                     cate_slug=p['cate_slug'], slug=p['slug'])
                for p in new_post
            ],

            cate_list = [
                dict
            ]
        )






@home.route('/')
def index():
    """
    Index page
    """
