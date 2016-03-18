# encoding: utf-8
from flask import render_template

from app.core.models import User, Post, Category, Tag
from app.core.service import *

class BaseSerive(object):
    def __init__(self):
        self.cate_data = self.get_cate_data()

    def paginate(self, data=[], page_index=1, per_page=12):
        # TODO: 错误处理
        try:
            offset = (page_index-1) * per_page
            res = data[offset:offset+per_page]
            return res
        except:
            return []

    def get_tag_data(self):
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

    def get_cate_data(self):
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

    def get_random_post(self):
        pass

class HomeServer(BaseSerive):

    def get_hot_posts(self):
        res = Post.query.order_by(func.random()).limit(11)
        return res

    def get_brief(model=Post, count=3):
        """
        TODO: 中文分片
        """
        pass

    def get_cate_posts(self, count=5):
        cates = Category.query.all()

        res = [
            dict(
                id=c.id,
                slug=c.slug,
                name=c.name,
                plist=[
                    dict(
                        id=p.id,
                        title=p.title,
                        slug=p.slug
                    )
                    for p in c.posts[:count]
                ]
            )
            for c in cates
        ]

        return res

class CatePageService(BaseSerive):
    def __init__(self, cslug, page_index=1):
        super(CatePageService, self).__init__()
        self.page_index = page_index
        self.cslug = cslug
        # TODO: error: if slug not exist?????
        self.cate = Category.query.filter_by(slug=self.cslug).first()

    def get_catepage_data(self):
        # TODO: post sorted???
        # TODO: 分页展示
        posts = self.paginate(self.cate.posts, self.page_index, 12)
        res = dict(
            cid=self.cate.id,
            slug=self.cate.slug,
            name=self.cate.name,
            page_num=self.page_index,
            plist=[
                dict(
                    id=p.id,
                    title=p.title,
                    slug=p.slug,
                    post_time=p.timestamp.strftime("%F %H:%M:%S"),
                    brief=u"中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？"
                    #TODO: brief???
                )
                for p in posts
            ],
        )
        return res

class TagPageService(BaseSerive):
    def __init__(self, tslug, page_num=1):
        super(CatePageService, self).__init__()
        self.page_num = page_num
        self.tslug = tslug
        # TODO: error: if slug not exist?????
        self.tag = Tag.query.filter_by(slug=self.tslug).first()

    def get_tagpage_data(self):
        posts = self.paginate(self.cate.posts, self.page_num, 12)
