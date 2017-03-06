# encoding: utf-8
import json

from sqlalchemy import func
from flask import request
from flask.views import MethodView

from app.core.views import TemplateView, DetailView, ListView
from app.core.models import Category
from app.core.base import *
from . import home


class TestView(TemplateView):
    template_name = 'index.jinja2'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        return context

home.add_url_rule('/test123/<string:slug>', view_func=TestView.as_view('test123'))


class IndexView(TemplateView):
    template_name = "home/index.jinja2"


class CategoryView(ListView):
    model = Post
    paginate_by = 10
    template_name = "home/category.jinja2"

    def get_basequery(self):
        basequery = super(CategoryView, self).get_basequery()
        slug = self.kwargs.get('slug')
        if not slug:
            abort(404)
        return basequery.filter(self.model.category.has(slug=slug))


class PostView(DetailView):
    model = Post
    template_name = 'home/post.jinja2'

    def get_basequery(self):
        basequery = super(PostView, self).get_basequery()
        cslug = self.kwargs.get('cslug')
        if cslug is None:
            abort(404)
        basequery = basequery.filter(self.model.category.has(slug=cslug))
        return basequery


index_view_func = IndexView.as_view('index')
home.add_url_rule('/', view_func=index_view_func)

category_view_func = CategoryView.as_view('category')
home.add_url_rule('/category/<string:slug>', view_func=category_view_func)
home.add_url_rule('/category/<string:slug>/page/<int:page>', view_func=category_view_func)

post_view_func = PostView.as_view('post')
home.add_url_rule('/<string:cslug>/<string:slug>.html', view_func=post_view_func )


@home.route('/test')
def test():
    # please test me
    # import pdb; pdb.set_trace()
    return json.dumps(str(test))


# @home.route('/')
# def index():
#     """
#     Index page
#     """
#     ser = HomeService()
#
#     context = dict(
#         nav=ser.cates,
#         cps=ser.get_cate_posts(),
#         hs=ser.get_random_posts(10),
#         briefs=ser.get_briefs(),
#         sidebar=dict(
#             new=ser.get_newest_posts(),
#             tags=ser.get_tags(),
#         )
#     )
#
#     # return json.dumps(context)
#     return render_template(
#         'index.jinja2',
#         ct=context
#     )


# @home.route('/category/<string:cslug>')
# @home.route('/category/<string:cslug>/page/<int:page>')
# def category(cslug, page=1):
#     ca = CatePageService(cslug, page)
#     catepage_data = ca.get_post_list()
#
#     context = dict(
#         nav=ca.cates,
#         cd=catepage_data,
#     )
#
#     return render_template(
#         'category.jinja2',
#         ct=context,
#     )


@home.route('/<int:year>/<string:month>', methods=['GET', 'POST'])
@home.route('/<int:year>/<string:month>/page/<int:page_num>', methods=['GET', 'POST'])
def archive(year, month, page_num=1):
    """
    Archive default page
    """
    return 'High & Dry'


# @home.route('/<string:cslug>/<string:pslug>.html', methods=['GET', 'POST'])
# def post(cslug, pslug):
#     """
#     post page
#     """
#     pp = PostPageService(cslug, pslug)
#     post_dict = pp.get_post()
#     comment_dict_list = pp.get_comments_data()
#     related_posts = pp.get_related_posts()
#
#     context = dict(
#         nav=pp.cates,
#         pd=post_dict,
#         cmds=comment_dict_list,
#         rel=related_posts,
#         random=pp.get_random_posts(),
#     )
#     # return json.dumps(related_posts)
#     return render_template(
#         'post.jinja2',
#         ct=context
#     )


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
