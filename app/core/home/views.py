# encoding: utf-8
from app.core.base import *

from . import home

@home.route('/')
def index():
    """
    Index page
    """
    cates = Category.query.all()
    hot_list = cates[1].posts[:11]
    random_brief = [
        {
            'id': p.id,
            'title': p.title,
            'slug': p.slug,
            'cslug': p.category.slug,
            'brief': p.body[:140],
        }
        for p in cates[2].posts[:3]
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

    new_plist = [
        {
            'id': p.id,
            'title': p.title,
            'slug': p.slug,
            'cslug': p.category.slug
        }
        for p in cates[4].posts[:10]
    ]

    cate_list = [
        {
            'id': c.id,
            'title': c.name,
            'slug': c.slug,
            'plist': [
                {
                    'id': p.id,
                    'title': p.title,
                    'slug': p.slug,
                    'cslug': p.category.slug
                }
                for p in c.posts[:5]
            ]
        }
        for c in cates
    ]

    tags = Tag.query.all()

    return render_template('index.jinja2', cates=cates, cate_list=cate_list,
                            hot_list=hot_list, random_brief=random_brief,
                            cate_sidebar=cate_sidebar, new_plist=new_plist, tags=tags)

@home.route('/category/<string:cslug>')
def index():
    return render_template('cate_list.jinja2')
