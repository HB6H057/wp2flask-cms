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
    from app.service.BaseService import PostService, CategoryService
    # import pdb; pdb.set_trace()
    p = PostService()
    kw = dict(
        tag_id=[
            13,
            26,
        ]
    )
    s = p.get_list(**kw)
    testerror
    return json.dumps(str(test))


@home.route('/')
def index():
    """
    Index page
    """
    hs = HomeService()

    cate_post_list = hs.get_cate_posts()
    hot_list = hs.get_hot_posts()
    brief_list = hs.get_brief()

    context = dict(
        nav=hs.cate_data,
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
    catepage_data = ca.get_catepage_data()

    context = dict(
        nav=ca.cate_data,
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

    post = Post.query.filter_by(slug=pslug).first()

    return render_template('post.jinja2', p=post)


@home.route('/tag/<string:tslug>', methods=['GET', 'POST'])
@home.route('/tag/<string:tslug>/page/<int:page>', methods=['GET', 'POST'])
def tag(tslug, page=1):
    """
    Tag default page
    """
    tps = TagPageService(tslug, page)
    tagpage_data = tps.get_tagpage_data()

    context = dict(
        nav=tps.cate_data,
        td=tagpage_data,
    )

    return render_template(
        'tag.jinja2',
        ct=context,
    )
