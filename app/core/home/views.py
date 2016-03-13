# encoding: utf-8
from app.core.base import *

from . import home

@home.route('/')
def index():
    """
    Index page
    """
    # import pdb; pdb.set_trace()

    tag_dict = BaseSerive.get_tag_data()

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
