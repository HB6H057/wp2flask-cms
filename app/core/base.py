# encoding: utf-8
from flask import render_template

from app.core.constants import *
from app.core.service import *
from app.core.models import User, Post, Category, Tag

class BasePageService(object):
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

    def get_value_by_special_key(self, d, sk):
        if sk == "post_count":
            v = d.posts.count()
        elif sk == "timestamp":
            v = d.timestamp.strftime("%F %H:%M:%S")
        elif sk == "font_size":
            # TODO: font_size function
            v = 3
        else:
            # TODO: log system
            print 'log keys = %s' % (sk)
            v = None

        return v

    def tag_dict_list_generator(self, data, key):
        # TODO: error
        dict_list = []

        for d in data:
            data_dict = {}
            for k in key:
                try:
                    data_dict[k] = getattr(d, k)
                except AttributeError:
                    data_dict[k] = self.get_value_by_special_key(d, k)
            dict_list.append(data_dict)

        return dict_list

        def post_list_page_data_generator(self, key):
            pass

        def post_list_data_generator(self, key):
            pass



class HomeServer(BasePageService):

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

class CatePageService(BasePageService):
    def __init__(self, cslug, page_num=1):
        super(CatePageService, self).__init__()
        self.page_num = page_num
        self.cslug = cslug
        # TODO: error: if slug not exist?????
        self.cate = Category.query.filter_by(slug=self.cslug).first()
        self.pagination = Post.query.filter(
            Post.category.has(slug=self.cslug)
        ).paginate(page=self.page_num, per_page=CAGE_PER_PAGE)

    def get_catepage_data(self):
        # TODO: post sorted???
        # TODO: 分页展示

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

class TagPageService(BasePageService):
    def __init__(self, tslug, page_num=1):
        super(CatePageService, self).__init__()
        self.page_num = page_num
        self.tslug = tslug
        # TODO: error: if slug not exist?????
        self.tag = Tag.query.filter_by(slug=self.tslug).first()

    def get_tagpage_data(self):
        # pagination =
        pass

class WidgetsService(BasePageService):

    def get_archive_data(self):
        # TODO: 是否抛弃这个功能？
        pass

    def get_newest_posts(self, count=10):
        posts = Post.query.limit(count).all()
        res = [
            dict(
                id=p.id,
                title=p.title,
                slug=p.slug,
                cslug=p.category.slug,
            )
            for p in posts
        ]

        return res
    def get_tag_data(self):
        """
        get tag data
        # TODO: tags sorted & limit
        """
        tags = Tag.query.all()

        tag_dict = self.tag_dict_list_generator(tags, TAG_WIDGET_DICT_KEY)

        return tag_dict

    def get_random_post(self, count):
        # TODO: 一次性取出所有文章，效率上能否优化？
        posts = Post.query.order_by(func.random()).all()[:count]

        res = [
            dict(
                id=p.id,
                title=p.title,
                slug=p.slug,
                cslug=p.category.slug,
            )
            for p in posts
        ]

        return res

    def get_related_posts(self):
        # TODO: wp-related-post 原理
        pass
