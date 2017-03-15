# encoding: utf-8

from flask import abort

from app.core.views import (
    TemplateView, DetailView, ModelFieldListView, ArchiveView
)
from app.core.models import Category, Tag, Post
from . import home


class TestView(TemplateView):
    template_name = 'index.jinja2'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        return context

home.add_url_rule('/test/<int:slug>/', view_func=TestView.as_view('test123'), methods=['GET', 'POST'])


class IndexView(TemplateView):
    template_name = "home/index.jinja2"


class CategoryView(ModelFieldListView):
    model = Category
    model_field = 'posts'
    paginate_by = 10
    template_name = "home/category.jinja2"


class TagView(ModelFieldListView):
    model = Tag
    model_field = 'posts'
    paginate_by = 10
    template_name = "home/tag.jinja2"


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


class ArchivePageView(ArchiveView):
    template_name = 'home/archive.jinja2'
    model = Post
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ArchivePageView, self).get_context_data(**kwargs)
        return context


# @home.route('/<int:year>/<string:month>', methods=['GET', 'POST'])
# @home.route('/<int:year>/<string:month>/page/<int:page_num>', methods=['GET', 'POST'])
# def archive(year, month, page_num=1):
#     """
#     Archive default page
#     """
#     return 'High & Dry'
