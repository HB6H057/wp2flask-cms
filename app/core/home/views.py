# encoding: utf-8
import json
from sqlalchemy import func
from flask import request
from app.core.base import *
from app.core.service import (CategoryService, PostService,
                              CommentService, TagService)
from . import home

@home.route('/test')
def test():
    ws = WidgetsService()
    d = ws.get_newest_posts()
    # import pdb; pdb.set_trace()
    # testerror
    return json.dumps(d)

@home.route('/')
def index():
    """
    Index page
    """
    hs = HomeServer()
    cate_list = hs.get_cate_posts()
    hot_list = hs.get_hot_posts()
    return render_template(
        'index.jinja2',
        cates=hs.cate_data,
        cate_list=cate_list,
        hot_list=hot_list
    )

@home.route('/category/<string:cslug>')
@home.route('/category/<string:cslug>/page/<int:page>')
def category(cslug, page=1):
    ca = CatePageService(cslug, page);
    catepage_data = ca.get_catepage_data()

    return render_template(
        'category.jinja2',
        catepage_data=catepage_data,
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
@home.route('/tag/<string:tslug>/page/<int:page_num>', methods=['GET', 'POST'])
def tag(tslug, page_num=1):
    """
    Tag default page
    """

    posts = Tag.query.filter_by(slug=tslug).one().posts
    plist = [
        dict(
            id=p.id,
            title=p.title,
            slug=p.slug,
            cslug=p.category.slug,
            brief=p.body[:360],
        )
        for p in posts
    ]

    return render_template('tag.jinja2', plist=plist)
