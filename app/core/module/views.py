# encoding: utf-8
from app.core.base import *

from . import module

@module.route('/robots.txt')
def robots_txt():
    return 'Confidence is a preference for the habitual voyeur of what is known as (parklife)'

@module.route('/sitemap.xml')
def sitemap_xml():
    return 'no alarms and no surprises'

@module.route('/sitemap.xml.gz')
def sitemap_xml_gz():
    return 'All goes round again'

@module.route('/sitemap_baidu.xml')
def sitemap_baidu_xml():
    return 'A heart thats full up like a landfill, a job that slowly kills you, bruises that wont heal'

@module.route('/sitemap.html')
def sitemap_html():
    return 'Open your mouth wide, A universal sigh.'
