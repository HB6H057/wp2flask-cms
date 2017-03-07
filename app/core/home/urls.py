# encoding: utf-8

from . import views, home

index_view_func = views.IndexView.as_view('index')
home.add_url_rule('/', view_func=index_view_func)

category_view_func = views.CategoryView.as_view('category')
home.add_url_rule('/category/<string:slug>', view_func=category_view_func)
home.add_url_rule('/category/<string:slug>/page/<int:page>', view_func=category_view_func)

tag_view_func = views.TagView.as_view('tag')
home.add_url_rule('/tag/<string:slug>', view_func=tag_view_func)
home.add_url_rule('/tag/<string:slug>/page/<int:page>', view_func=tag_view_func)

post_view_func = views.PostView.as_view('post')
home.add_url_rule('/<string:cslug>/<string:slug>.html', view_func=post_view_func )

archive_view_func = views.ArchivePageView.as_view('archive')
home.add_url_rule('/<int:year>/<string:month>', view_func=archive_view_func)
home.add_url_rule('/<int:year>/<string:month>/page/<int:page_num>', view_func=archive_view_func )
home.add_url_rule('/<int:year>', view_func=archive_view_func)
home.add_url_rule('/<int:year>/page/<int:page_num>', view_func=archive_view_func )




