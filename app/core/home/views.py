# encoding: utf-8
import json
from sqlalchemy import func
from flask import request
from app.core.base import *
# from app.core.service import (CategoryService, PostService,
#                               CommentService, TagService)
from . import home


@home.route('/test')
def test():
    # please test me
    # import pdb; pdb.set_trace()
    return json.dumps(str(test))


@home.route('/')
def index():
    """
    Index page
    """
    hs = HomeService()

    cate_post_list = hs.get_cate_posts()
    hot_list = hs.get_random_posts(10)
    brief_list = hs.get_briefs()

    context = dict(
        nav=hs.cates,
        cps=cate_post_list,
        hs=hot_list,
        briefs=brief_list,
    )

    # return json.dumps(context)
    return render_template(
        'index.jinja2',
        ct=context
    )


@home.route('/category/<string:cslug>')
@home.route('/category/<string:cslug>/page/<int:page>')
def category(cslug, page=1):
    ca = CatePageService(cslug, page)
    catepage_data = ca.get_post_list()

    context = dict(
        nav=ca.cates,
        cd=catepage_data,
    )

    return render_template(
        'category.jinja2',
        ct=context,
    )


@home.route('/<int:year>/<string:month>', methods=['GET', 'POST'])
@home.route('/<int:year>/<string:month>/page/<int:page_num>', methods=['GET', 'POST'])
def archive(year, month, page_num=1):
    """
    Archive default page
    """
    return 'High & Dry'


@home.route('/<string:cslug>/<string:pslug>.html', methods=['GET', 'POST'])
def post(cslug, pslug):
    """
    post page
    """
    pp = PostPageService(cslug, pslug)
    post_dict = pp.get_post()
    comment_dict_list = pp.get_comments_data()
    related_posts = pp.get_related_posts()

    context = dict(
        nav=pp.cates,
        pd=post_dict,
        cmds=comment_dict_list,
    )
    # return json.dumps(comment_dict_list)
    return render_template(
        'post.jinja2',
        ct=context
    )


@home.route('/tag/<string:tslug>', methods=['GET', 'POST'])
@home.route('/tag/<string:tslug>/page/<int:page>', methods=['GET', 'POST'])
def tag(tslug, page=1):
    """
    Tag default page
    """
    tps = TagPageService(tslug, page)
    tagpage_data = tps.get_post_list()

    context = dict(
        nav=tps.cates,
        td=tagpage_data,
    )

    return render_template(
        'tag.jinja2',
        ct=context,
    )
