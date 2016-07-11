# encoding: utf-8
import lxml.html
import re

from flask import render_template, abort

from app.core.constants import *
# from app.core.service import *
from sqlalchemy import func
from app.core.models import User, Post, Category, Tag

html = u'''
<tbody>
<tr>
<td width="127" valign="top"><strong>核心知识</strong></td>
<td colspan="2" width="441" valign="top"><strong>课标解读</strong><strong>&nbsp;</strong></td>
</tr>
<tr>
<td rowspan="4" width="127" valign="top">力的概念</td>
<td width="36" valign="top">1</td>
<td width="405" valign="top">理解力是物体之间的相互作用，能找出施力物体和受力物体．</td>
</tr>
<tr>
<td width="36" valign="top">2</td>
<td width="405" valign="top">知道力的作用效果．</td>
</tr>
<tr>
<td width="36" valign="top">3</td>
<td width="405" valign="top">知道力有大小和方向，会画出力的图示或力的示意图．</td>
</tr>
<tr>
<td width="36" valign="top">4</td>
<td width="405" valign="top">知道力的分类．</td>
</tr>
<tr>
<td rowspan="3" width="127" valign="top">重力的确概念</td>
<td width="36" valign="top">5</td>
<td width="405" valign="top">知道重力是地面附近的物体由于受到地球的吸引而产生的．</td>
</tr>
<tr>
<td width="36" valign="top">6</td>
<td width="405" valign="top">知道重力的大小和方向，会用公式<em>Ｇ＝ｍｇ</em>计算重力．</td>
</tr>
<tr>
<td width="36" valign="top">7</td>
<td width="405" valign="top">知道重心的概念以及均匀物体重心的位置．</td>
</tr>
<tr>
<td rowspan="3" width="127" valign="top">弹力的概念</td>
<td width="36" valign="top">8</td>
<td width="405" valign="top">知道什么是弹力以及弹力产生的条件．</td>
</tr>
<tr>
<td width="36" valign="top">9</td>
<td width="405" valign="top">能在力的图示（或力的示意图）中正确画出弹力的方向．</td>
</tr>
<tr>
<td width="36" valign="top">10</td>
<td width="405" valign="top">知道如何显示微小形变．</td>
</tr>
<tr>
<td rowspan="3" width="127" valign="top">胡克定律</td>
<td width="36" valign="top">11</td>
<td width="405" valign="top">知道在各种形变中，形变越大，弹力越大．</td>
</tr>
<tr>
<td width="36" valign="top">12</td>
<td width="405" valign="top">知道胡克定律的内容和适用条件．</td>
</tr>
<tr>
<td width="36" valign="top">13</td>
<td width="405" valign="top">对一根弹簧，会用公式<em>ｆ＝ｋｘ</em>进行计算．</td>
</tr>
<tr>
<td rowspan="4" width="127" valign="top">摩擦力的概念</td>
<td width="36" valign="top">14</td>
<td width="405" valign="top">知道滑动摩擦力产生的条件，会判断滑动摩擦力的方向．</td>
</tr>
<tr>
<td width="36" valign="top">15</td>
<td width="405" valign="top">会利用公式<em>ｆ＝μＮ</em>进行计算，知道动摩擦因数跟什么有关</td>
</tr>
<tr>
<td width="36" valign="top">16</td>
<td width="405" valign="top">知道静摩擦产生的条件，会判断静摩擦力的方向．</td>
</tr>
<tr>
<td width="36" valign="top">17</td>
<td width="405" valign="top">知道最大静摩擦力跟两物间的压力成正比</td>
</tr>
<tr>
<td rowspan="2" width="127" valign="top">二力平衡</td>
<td width="36" valign="top">18</td>
<td width="405" valign="top">知道什么是力的平衡．</td>
</tr>
<tr>
<td width="36" valign="top">19</td>
<td width="405" valign="top">知道二力平衡的条件．</td>
</tr>
<tr>
<td rowspan="7" width="127" valign="top">力的合成和分解</td>
<td width="36" valign="top">20</td>
<td width="405" valign="top">理解力的合成和合力的概念．</td>
</tr>
<tr>
<td width="36" valign="top">21</td>
<td width="405" valign="top">理解力的合成和合力的概念．</td>
</tr>
<tr>
<td width="36" valign="top">22</td>
<td width="405" valign="top">掌握平行四边形定则，会用作图法、公式法求合力的大小和方向．</td>
</tr>
<tr>
<td width="36" valign="top">23</td>
<td width="405" valign="top">熟悉力的三角形法．</td>
</tr>
<tr>
<td width="36" valign="top">24</td>
<td width="405" valign="top">掌握平行四边形定则．</td>
</tr>
<tr>
<td width="36" valign="top">25</td>
<td width="405" valign="top">理解力的分解和分力的概念．理解力的分解是力的合成逆运算，</td>
</tr>
<tr>
<td width="36" valign="top">26</td>
<td width="405" valign="top">会用作图法求分力，会用直角三角形的知识计算分力</td>
</tr>
<tr>
<td rowspan="2" width="127" valign="top">矢量和标量及运算</td>
<td width="36" valign="top">27</td>
<td width="405" valign="top">知道什么是矢量，什么是标量．</td>
</tr>
<tr>
<td width="36" valign="top">28</td>
<td width="405" valign="top">知道平行四边形定则是矢量加法运算的普遍定则．</td>
</tr>
<tr>
<td width="127" valign="top">受力分析</td>
<td width="36" valign="top">2</td>
<td width="405" valign="top">初步熟悉物体的受力分析．</td>
</tr>
</tbody>
'''


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
            # TODO: 考虑把截断字符的任务放到views.py
            v = self.briefy(html, 50)
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
        # TODO: error
        dict_list = []

        for d in data:
            data_dict = self.data_dict_generator(d, key)
            dict_list.append(data_dict)

        return dict_list

    def post_list_page_data_generator(self, d, key, pkey):
        """
        文章列表页面数据: {'id':'1', ....., 'plist':[{....}, {....}, ....]}
        """
        d_dict = self.data_dict_generator(d, key)
        plist = self.data_dict_list_generator(self.pagination.items, pkey)
        d_dict['plist'] = plist

        return d_dict


class WidgetsMiXin(DataGeneratorMixin):
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

    def get_random_posts(self, count=10):
        posts = Post.query.order_by(
            func.random()
        ).limit(count).all()

        post_dict_list = self.data_dict_list_generator(
            posts,
            POST_DICT_KEY
        )

        return post_dict_list


class BasePageService(DataGeneratorMixin):

    def __init__(self):
        self.cate_data = self.get_cate_data()
        self.pagination = None

    def briefy(self, body, count):
        # TODO: 效率不知道高不高，只能先这样了
        v = lxml.html.fromstring(body)
        text = v.text_content()
        text = re.sub("(\s)+", " ", text)
        return text[:count]

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


class HomeService(BasePageService, WidgetsMiXin):

    def get_brief(self, count=3):
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
        self.cate = Category.query.filter_by(slug=self.cslug).first()
        if self.cate is None:
            abort(404)
        self.pagination = Post.query.filter(
            Post.category.has(slug=self.cslug)
        ).paginate(page=self.page_num, per_page=CAGE_PER_PAGE)

    def get_catepage_data(self):
        # TODO: post sorted???
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


class PostPageService(BasePageService):
    # 李白喝酒写的诗,都是三分豪气四分爽利五分恣意,舍我其谁。，我喝酒写代码，z z z z z z z
    def __init__(self, cslug, pslug):
        # BUG: 检测cslug
        super(PostPageService, self).__init__()
        self.post = Post.query.filter_by(
            slug=pslug,
        ).first()

    def get_post_data(self):
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
