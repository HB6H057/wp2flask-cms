# encoding: utf-8
from flask import render_template

from app.core.models import User, Post, Category, Tag

class BaseSerive(object):
    @staticmethod
    def get_newest_posts(slug=None, model=Post, count=3):
        """
        get newest posts
        BUG: if slug not exits or ..
        """
        if model == Post:
            import pdb; pdb.set_trace()
        
            posts = Post.query.limit(count).all()

            posts_data = [
                dict(
                    id=p.id,
                    title=p.title,
                    slug=p.slug,
                )
                for p in posts
            ]

        else:
            cate = model.query.filter_by(slug=slug).one()
            posts = cate.posts[:count]

            posts_data = dict(
                id=cate.id,
                slug=cate.slug,
                name=cate.name,
                plist=[
                    dict(
                        id=p.id,
                        title=p.title,
                        slug=p.slug,
                    )
                    for p in posts
                ],
            )

        return posts_data

    @staticmethod
    def get_tag_data():
        """
        get tag data
        """
        tags = Tag.query.all()

        tag_dict = [
            dict(
                id=t.id,
                name=t.name,
                slug=t.slug,
                count=t.posts.count()
            )
            for t in tags
        ]

        return tag_dict

    @staticmethod
    def get_cate_data():
        """
        get category data
        TODO: finish sorted function
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
    def random_get_data(model=Post, count=3):
        """
        Random get data (no finish)
        """
        return model.query.limit(count).all()

class HomeServer(object):

    @staticmethod
    def get_hot_posts(model=Post, count=3):
        pass

    @staticmethod
    def get_brief(model=Post, count=3):
        pass

    @staticmethod
    def get_cate_posts(count=5):
        pass
