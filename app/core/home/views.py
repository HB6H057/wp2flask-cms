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
    import pdb; pdb.set_trace()
    Post.query.limit(11).order_By(fun.random()).all()

@home.route('/api')
def api():


    # c = CategoryService()
    # d = c.get_cate_list()
    # d = c.get_cate_by_cid(2)
    # d = c.get_cate_by_cid(2)
    # d = c.get_posts_by_cid(2)

    c = PostService()
    d = c.get_post_list(request.args)
    # d = c.get_post_by_pid(2)
    # d = c.get_cate_of_post(2)
    # d = c.get_comments_of_post(2)

    # c = CommentService()
    # d = c.get_comment_list()
    # d = c.get_comment_by_cmid(2)
    # d = c.get_post_by_cmid(2)

    # c = TagService()
    # d = c.get_tag_list()
    # d = c.get_posts_by_tid(2)


    return json.dumps(d)

@home.route('/')
def index():
    """
    Index page
    """
    ps = PostService()
    hostlist = ps.get_post_list(dict(
        limit=11,
        random='true'
    ))

    import pdb; pdb.set_trace()

    return render_template('index.jinja2')

@home.route('/category/<string:cslug>')
def category(cslug):
    cates = Category.query.all()
    cate_posts = Category.query.filter_by(slug=cslug).one().posts

    plist = [
        dict(
            id=p.id,
            title=p.title,
            slug=p.slug,
            cslug=p.category.slug,
            brief=p.body[:360],
        )
        for p in cate_posts
    ]

    cate_sidebar = [
        {
            'id': c.id,
            'title': c.name,
            'slug': c.slug,
            'count': c.posts.count()
        }
        for c in cates
    ]

    tags = Tag.query.all()

    return render_template('category.jinja2', cates=cates, plist=plist,
                            cate_sidebar=cate_sidebar, tags=tags
                          )

@home.route('/<int:year>/<string:month>', methods=['GET', 'POST'])
def archive(year, month):
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
def tag(tslug):
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
