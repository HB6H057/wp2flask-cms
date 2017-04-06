# encoding: utf-8
from markdown import markdown

from wtforms import TextAreaField
from jinja2 import Markup
from flask_admin import expose, BaseView
from flask_admin.contrib.sqla import ModelView

from app.core.models import Post, Category, Tag


def tags_formatter(view, context, model, name):
    return ", ".join(map(lambda t: t.name, model.tags))


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin_template/admin.html')


class PostView(ModelView):
    page_size = 10
    column_default_sort = ('update_time', True)
    column_list = ('title', 'category', 'tags', 'update_time', )
    form_columns = ('title', 'slug', 'tags', 'category', 'body', )
    column_searchable_list = ('title', )
    column_filters = ('category', )

    column_formatters = dict(
        category=lambda v, c, m, p: m.category.name,
        update_time=lambda v, c, m, p: m.update_time.strftime(u'%Y-%m-%d'),
        tags=tags_formatter,
    )

    column_labels = {
        'title': u'标题',
        'category': u'分类',
        'update_time': u'更新时间',
        'body': u'内容',
        'tags': u'标签',
    }

    def get_form(self):
        form = super(PostView, self).get_form()
        form.body = TextAreaField(render_kw={'rows': 20})
        return form

    def __init__(self, session, **kwargs):
        super(PostView, self).__init__(Post, session, **kwargs)


class CategoryView(ModelView):
    page_size = 10
    column_list = ('name', 'description', 'post_count', )
    form_columns = ('name', 'slug', 'description', )
    column_searchable_list = ('name', )
    column_formatters = {
        'post_count': lambda v, c, m, p: Markup('<a herf="/admin/post/?flt2_9=%s">%s</a>' % (m.slug, m.posts.count()))
    }
    column_labels = {
        'name': u'分类',
        'description': u'描述',
        'post_count': u'文章数量',
    }

    def __init__(self, session, **kwargs):
        super(CategoryView, self).__init__(Category, session, **kwargs)


class TagView(ModelView):
    page_size = 10
    column_list = ('name', 'post_count', )
    form_columns = ('name', 'slug', )
    column_searchable_list = ('name', )
    column_formatters = {
        'post_count': lambda v, c, m, p: Markup('<a herf="/admin/post/?flt2_9=%s">%s</a>' % (m.slug, m.posts.count()))
    }
    column_labels = {
        'name': u'标签',
        'post_count': u'文章数量',
    }

    def __init__(self, session, **kwargs):
        super(TagView, self).__init__(Tag, session, **kwargs)
