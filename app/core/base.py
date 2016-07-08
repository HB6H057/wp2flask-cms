# encoding: utf-8
from flask import render_template

from app.core.constants import *
# from app.core.service import *
from sqlalchemy import func
from app.core.models import User, Post, Category, Tag


class BasePageService(object):

    def __init__(self):
        self.cate_data = self.get_cate_data()
        self.pagination = None

    def briefy(self, body, count):
        # TODO: 编码问题 && html标签问题
        return body[:count]

    def get_cate_data(self):
        """
        get category data
        TODO: finish sorted function
        """
        cates = Category.query.all()

        cate_dict_list = self.data_dict_list_generator(
            cates,
            CATEGORY_DICT_KEY
        )

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
            v = self.briefy(v, 80)
        elif sk == "font_size":
            # TODO: font_size function
            v = 3
        else:
            # TODO: log system
            print 'log keys = %s' % (sk)
            v = None

        return v

    def data_dict_generator(self, d, key):
        """
            数据字典化
        """
        data_dict = {}
        for k in key:
            try:
                data_dict[k] = getattr(d, k)
            except AttributeError:
                data_dict[k] = self.get_value_by_special_key(d, k)
        return data_dict

    def data_dict_list_generator(self, data, key):
        """
            数据字典化列表
        """
        # TODO: error
        dict_list = []

        for d in data:
            data_dict = self.data_dict_generator(d, key)
            dict_list.append(data_dict)

        return dict_list

    def post_list_page_data_generator(self, d, key, pkey):
        """
            文章列表页面数据
        """
        d_dict = self.data_dict_generator(d, key)
        plist = self.data_dict_list_generator(self.pagination.items, pkey)
        d_dict['plist'] = plist

        return d_dict


class HomeService(BasePageService):

    def get_hot_posts(self):
        posts = Post.query.order_by(
            func.random()
        ).limit(HOME_HOT_POSTS_NUM).all()

        post_dict_list = self.data_dict_list_generator(
            posts,
            POST_DICT_KEY,
        )

        return post_dict_list

    def get_brief(self, count=3):
        # TODO: 保证随机性
        posts = Post.query.limit(count).all()

        brief_dict_list = self.data_dict_list_generator(
            posts,
            POST_BRIEF_DICT_KEY
        )

        return brief_dict_list

    def get_cate_posts(self, count=5):
        cates = Category.query.all()

        cate_post_dict_list = []

        for c in cates:
            cate_dict = self.data_dict_generator(
                c,
                CATEGORY_DICT_KEY
            )
            cate_dict['plist'] = self.data_dict_list_generator(
                c.posts[:count],
                POST_DICT_KEY
            )

            cate_post_dict_list.append(cate_dict)

        return cate_post_dict_list


class CatePageService(BasePageService):

    def __init__(self, cslug, page_num=1):
        super(CatePageService, self).__init__()
        self.page_num = page_num
        self.cslug = cslug
        # TODO: error: if slug not exist?????
        # TODO: BUG: 会自动包含favicon.ico(访问/category/favicon.ico)
        self.cate = Category.query.filter_by(slug=self.cslug).first()
        self.pagination = Post.query.filter(
            Post.category.has(slug=self.cslug)
        ).paginate(page=self.page_num, per_page=CAGE_PER_PAGE)

    def get_catepage_data(self):
        # TODO: post sorted???
        # TODO: 分页展示
        post_list_dict = self.post_list_page_data_generator(
            self.cate,
            CATEGORY_PAGE_DICT_KEY,
            POST_BRIEF_DICT_KEY,
        )

        return post_list_dict


class TagPageService(BasePageService):
    def __init__(self, tslug, page_num=1):
        super(TagPageService, self).__init__()
        self.page_num = page_num
        self.tslug = tslug
        # TODO: error: if slug not exist?????
        self.tag = Tag.query.filter_by(slug=self.tslug).first()
        # TODO: bug
        self.pagination = Post.query.filter(
            Post.tags.any(slug=self.tslug)
        ).paginate(page=self.page_num, per_page=TAG_PER_PAGE)

    def get_tagpage_data(self):
        post_list_dict = self.post_list_page_data_generator(
            self.tag,
            CATEGORY_PAGE_DICT_KEY,
            POST_BRIEF_DICT_KEY,
        )

        return post_list_dict


class WidgetsService(BasePageService):

    def get_archive_data(self):
        # TODO: 是否抛弃这个功能？
        pass

    def get_newest_posts(self, count=10):
        posts = Post.query.limit(count).all()

        post_dict_list = self.data_dict_list_generator(
            posts,
            POST_DICT_KEY
        )

        return post_dict_list

    def get_tag_data(self):
        """
        get tag data
        """
        # TODO: tags sorted & limit
        tags = Tag.query.all()

        tag_dict_list = self.data_dict_list_generator(
            tags,
            TAG_WIDGET_DICT_KEY
        )

        return tag_dict_list

    def get_random_post(self, count=10):
        # TODO: 一次性取出所有文章，效率上能否优化？
        posts = Post.query.order_by(func.random()).all()[:count]

        post_dict_list = self.data_dict_list_generator(
            posts,
            POST_DICT_KEY
        )

        return post_dict_list

    def get_related_posts(self):
        # TODO: wp-related-post 原理
        pass
