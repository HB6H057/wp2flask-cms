# encoding: utf-8
import lxml.html
import re

from flask import render_template, abort

from app.core.constants import *
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from app.core.models import User, Post, Category, Tag


class DataGeneratorMixin(object):
    '''
    数据生成器Mixin, 用于打包数据。
    '''
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
            v = self.briefy(HTML)
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
        数据字典化: {'id':'1', 'name':'radiohead', ....}
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
        数据字典化列表: [{'id':'1', 'name':'radiohead', ....}, {...}, ...]
        """
        dict_list = []

        for d in data:
            data_dict = self.data_dict_generator(d, key)
            dict_list.append(data_dict)

        return dict_list

    def post_list_page_data_generator(self, d, key, pkey):
        """
        文章列表页面数据: {'id':'1', ....., 'plist':[{....}, {....}, ....]}
        """
        data_dict = self.data_dict_generator(d, key)
        plist = self.data_dict_list_generator(self.pagination.items, pkey)
        data_dict['plist'] = plist

        return data_dict

    def briefy(self, body):
        '''
        生成摘要
        '''
        html_str = lxml.html.fromstring(body)
        text = html_str.text_content()
        text = re.sub("(\s)+", " ", text)
        return text


class WidgetsMiXin(DataGeneratorMixin):
    def get_archives(self):
        # TODO: 是否抛弃这个功能？
        pass

    def get_newest_posts(self, count=10):
        posts = Post.query.limit(count).all()

        post_dict_list = self.data_dict_list_generator(
            posts,
            POST_DICT_KEY
        )

        return post_dict_list

    def get_tags(self):
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

    def get_random_posts(self, count=10):
        posts = Post.query.order_by(
            func.random()
        ).limit(count).all()

        post_dict_list = self.data_dict_list_generator(
            posts,
            POST_DICT_KEY
        )

        return post_dict_list


class BaseService(DataGeneratorMixin):
    """
    页面serviceBaseClass
    self.cates: 分类信息用于导航栏
    """
    def __init__(self):
        self.cates = self.get_cates()

    def get_cates(self):
        """
        get category data
        """
        cates = Category.query.all()

        cate_dict_list = self.data_dict_list_generator(
            cates,
            CATEGORY_DICT_KEY
        )

        return cate_dict_list


class HomeService(BaseService, WidgetsMiXin):

    def get_briefs(self, count=3):
        # TODO: 保证随机性
        posts = Post.query.order_by(
            func.random()
        ).limit(count).all()

        brief_dict_list = self.data_dict_list_generator(
            posts,
            POST_BRIEF_DICT_KEY
        )

        return brief_dict_list

    def get_cate_posts(self, count=5):
        # TODO: cates 两次query 效率不行
        cates = Category.query.all()

        cate_post_dict_list = []
        # TODO: 这里是不是专门有个数据生成器？
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


class ListPageService(BaseService, WidgetsMiXin):
    '''
    文章列表页面鸡肋
    '''
    # TODO: 抽象类
    def __init__(self, slug, page=1):
        super(ListPageService, self).__init__()
        self.page = page
        self.slug = slug
        self.obj = None

    def get_post_list(self):
        post_list_dict = self.post_list_page_data_generator(
            self.obj,
            CATEGORY_PAGE_DICT_KEY,
            POST_BRIEF_DICT_KEY,
        )

        return post_list_dict


class CatePageService(ListPageService):
    """
    分类页面
    """
    def __init__(self, slug, page=1):
        super(CatePageService, self).__init__(slug=slug, page=page)

        try:
            self.obj = Category.query.filter_by(slug=self.slug).one()
        except NoResultFound:
            # TODO: LOGGING
            abort(404)
        except MultipleResultsFound:
            # TODO: LOGGING
            abort(404)

        self.pagination = Post.query.filter(
            Post.category.has(slug=self.slug)
        ).paginate(page=self.page, per_page=CAGE_PER_PAGE)


class TagPageService(ListPageService):
    def __init__(self, slug, page=1):
        super(TagPageService, self).__init__(slug=slug, page=page)
        self.page = page
        self.slug = slug

        try:
            self.obj = Tag.query.filter_by(slug=self.slug).first()
        except NoResultFound:
            # TODO: LOGGING
            abort(404)
        except MultipleResultsFound:
            # TODO: LOGGING
            abort(404)

        self.pagination = Post.query.filter(
            Post.tags.any(slug=self.slug)
        ).paginate(page=self.page, per_page=TAG_PER_PAGE)


class PostPageService(BaseService):
    # 李白喝酒写的诗,都是三分豪气四分爽利五分恣意,舍我其谁。，我喝酒写的代码，zzzzzz
    def __init__(self, cslug, pslug):
        # BUG: 检测cslug,一会一起做
        super(PostPageService, self).__init__()

        try:
            self.post = Post.query.filter_by(slug=pslug).one()
        except NoResultFound:
            # TODO: LOGGING
            abort(404)
        except MultipleResultsFound:
            # TODO: LOGGING
            abort(404)

    def get_post(self):
        post_dict = self.data_dict_generator(self.post, POST_PAGE_DICT_KEY)
        return post_dict

    def get_comments_data(self):
        comment_dict_list = self.data_dict_list_generator(
            self.post.comments,
            COMMENT_DICT_KEY
        )

        return comment_dict_list

    def get_related_posts(self, count=10):
        # TODO: 原理：取同分类下第一个tag相同的文章，然后再文本相似度计算（后者先不做）
        # TODO: 未完成
        related_posts = Post.query.filter_by(
            category_id=self.post.category_id,
        ).limit(count).all()

        return related_posts
