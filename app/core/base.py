# encoding: utf-8
from flask import render_template

from app.core.models import User, Post, Category, Tag

class BaseSerive(object):
    @staticmethod
    def get_cate_data(self):
        """
        get category data
        TODO: sorted function
        """
        cates = Category.query.all()

        nav_dict = [
            dict(
                id=c.id,
                name=c.name,
                slug=c.slug,
                count=c.posts.count()
            )
            for c in cates
        ]

        return nav_dict
    @staticmethod
    def random_get_data(self, model=Post, count=3):
        """
        Random get data (no finish)
        """
        return model.query.limit(count).all()
