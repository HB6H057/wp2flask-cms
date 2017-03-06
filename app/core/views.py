# encoding: utf-8
from flask.views import MethodView
from flask import request, render_template, abort
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


class View(MethodView):

    def dispatch_request(self, *args, **kwargs):
        self.kwargs = kwargs
        self.args = args
        self.request = request
        return super(View, self).dispatch_request(*args, **kwargs)


class TemplateResponseMixin(object):
    template_name = None

    def get_template_name(self):
        if self.template_name:
            return self.template_name
        return {}

    def render_to_response(self, context):
        return render_template(
            self.get_template_name(),
            **context
        )


class ContextMixin(object):
    def get_context_data(self, **kwargs):
        if 'view' not in kwargs.keys():
            kwargs['view'] = self

        return kwargs


class MultipleObjectMixin(ContextMixin):
    model = None
    paginate_by = None
    page_kwarg = 'page'
    ordering = None

    def get_context_data(self, **kwargs):
        context = dict()
        if self.object_list is not None:
            context['object_list'] = self.object_list
        context.update(kwargs)
        return super(MultipleObjectMixin, self).get_context_data(**context)

    def get_basequery(self):
        if self.model is not None:
            return self.model.query
        else:
            raise ValueError("model is None")

    def get_page_kwargs(self):
        return self.page_kwarg

    def get_ordering(self):
        return self.ordering


class SingleObjectMixin(ContextMixin):
    model = None
    pk_url_kwarg = 'id'
    slug_url_kwarg = 'slug'

    def get_object(self, basequery=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if basequery is None:
            basequery = self.model.query

        if slug is not None:
            basequery = basequery.filter_by(slug=slug)
        if pk is not None:
            basequery = basequery.filter_by(slug=slug)
        if slug is None and pk is None:
            raise ValueError("bad feel")
        try:
            obj = basequery.one()
        except NoResultFound:
            abort(404)
        except MultipleResultsFound:
            raise MultipleResultsFound
        return obj

    def get_context_data(self, **kwargs):
        context = dict()
        if self.object is not None:
            context['object'] = self.object
        context.update(kwargs)
        return super(SingleObjectMixin, self).get_context_data(**context)


class SingleObjectFieldListMixin(SingleObjectMixin, MultipleObjectMixin):
    model_field = None

    def get_basequery(self, obj=None):
        model_field = self.get_model_field()
        if model_field is None:
            raise ValueError, 'bad feel'
        if obj is None:
            obj = self.get_object()
        basequery = getattr(obj, model_field)
        return basequery

    def get_model_field(self):
        return self.model_field


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    def get(self, **kwargs):
        return self.render_to_response(
            self.get_context_data(**kwargs)
        )


class DetailView(SingleObjectMixin, TemplateResponseMixin, View):
    def get(self, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(**dict(context=context))


class ListView(MultipleObjectMixin, TemplateView, View):
    def get(self, *args, **kwargs):
        # self.object_list = self.get_basequery()
        basequery = self.get_basequery()
        page_kwargs = self.get_page_kwargs()
        page = self.kwargs.get(page_kwargs) or 1
        self.object_list = basequery.paginate(page, self.paginate_by)
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(**dict(context=context))


class ModelFieldListView(SingleObjectFieldListMixin, TemplateView, View):
    def get(self, *args, **kwargs):
        obj = self.get_object()
        basequery = self.get_basequery(obj=obj)

        page_kwargs = self.get_page_kwargs()
        page = self.kwargs.get(page_kwargs) or 1

        self.object = obj
        self.object_list = basequery.paginate(page, self.paginate_by)

        context = self.get_context_data(object_list=self.object_list, object=self.object)
        return self.render_to_response(**dict(context=context))


class ArchiveView(View):
    pass



