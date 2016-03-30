# encoding: utf-8
from app.core.base import *
from flask import send_from_directory, request

from . import module


@module.route('/sitemap.xml')
@module.route('/robots.txt')
@module.route('/sitemap_baidu.xml')
@module.route('/sitemap.html')
def robots_txt():
    return send_from_directory(module.static_folder, request.path[1:])


@module.route('/sitemap.xml.gz')
def sitemap_xml_gz():
    return 'All goes round again'
