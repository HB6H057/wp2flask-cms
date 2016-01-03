# encoding: utf-8
from app.core.base import *

from . import home

def test():
    title = u'2016目标是早睡早起作息规律按时吃饭'
    return render_template('test.jinja2', title=title)

@home.route('/')
def index():
    """
    Index page
    """
    
    title = u'2016目标是早睡早起作息规律按时吃饭'

    return render_template('test.jinja2', title=title)
