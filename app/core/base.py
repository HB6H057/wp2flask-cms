# encoding: utf-8
from flask import render_template

from app.core.constants import *
from app.core.service import *
from app.core.models import User, Post, Category, Tag

class BasePageService(object):
    def __init__(self):
        self.cate_data = self.get_cate_data()
        self.pagination = None

    def get_cate_data(self):
        """
        get category data
        TODO: finish sorted function
        """
        cates = Category.query.all()

        cate_dict_list = self.data_dict_list_generator(cates, CATEGORY_DICT_KEY)

        return cate_dict_list

    def get_value_by_special_key(self, d, sk):
        if sk == "post_count":
            v = d.posts.count()
        elif sk == "pagination":
            v = self.pagination
        elif sk == "cslug":
            v = d.category.slug
        elif sk == "create_date":
            v = d.timestamp.strftime("%F %H:%M:%S")
        elif sk == "brief":
            # TODO: brief function
            v = u"第八单元  19世纪以来的世界文学艺术  第22课  文学的繁荣  【基础解读】  一、浪漫主义文学     1、浪漫主义文学产生的背景：   （1）18世纪末至19世纪30年代，欧洲革命和战争不断，社会动乱不已。  （2）政治中的黑暗，社会的不平等，使人们感到法国大革命后确立的资本主义制度远不如启..."
        elif sk == "font_size":
            # TODO: font_size function
            v = 3
        else:
            # TODO: log system
            print 'log keys = %s' % (sk)
            v = None

        return v

    def data_dict_generator(self, d, key):
        data_dict = {}
        for k in key:
            try:
                data_dict[k] = getattr(d, k)
            except AttributeError:
                data_dict[k] = self.get_value_by_special_key(d, k)
        return data_dict

    def data_dict_list_generator(self, data, key):
        # TODO: error
        dict_list = []

        for d in data:
            data_dict = self.data_dict_generator(d, key)
            dict_list.append(data_dict)

        return dict_list

    def post_list_page_data_generator(self, d, key, pkey):
        d_dict = self.data_dict_generator(d, key)
        plist = self.data_dict_list_generator(self.pagination.items, pkey)
        d_dict['plist'] = plist

        return d_dict

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

        # res = dict(
        #     cid=self.cate.id,
        #     slug=self.cate.slug,
        #     name=self.cate.name,
        #     page_num=self.page_index,
        #     plist=[
        #         dict(
        #             id=p.id,
        #             title=p.title,
        #             slug=p.slug,
        #             post_time=p.timestamp.strftime("%F %H:%M:%S"),
        #             brief=u"中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？中文分词改如何做？"
        #             #TODO: brief???
        #         )
        #         for p in posts
        #     ],
        # )

        post_list_dict = self.post_list_page_data_generator(
            self.cate,
            CATEGORY_PAGE_DICT_KEY,
            POST_BRIEF_DICT_KEY,
        )

        return post_list_dict
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

        post_dict_list = self.data_dict_list_generator(posts, POST_DICT_KEY)

        return post_dict_list

    def get_tag_data(self):
        """
        get tag data
        """
        # TODO: tags sorted & limit
        tags = Tag.query.all()

        tag_dict_list = self.data_dict_list_generator(tags, TAG_WIDGET_DICT_KEY)

        return tag_dict_list

    def get_random_post(self, count=10):
        # TODO: 一次性取出所有文章，效率上能否优化？
        posts = Post.query.order_by(func.random()).all()[:count]

        post_dict_list = self.data_dict_list_generator(posts, POST_DICT_KEY)

        return post_dict_list

    def get_related_posts(self):
        # TODO: wp-related-post 原理
        pass
