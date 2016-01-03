# encoding: utf-8
from flask import render_template

from app.core.models import User
class BaseViews(object):
    def test(self):
        title = '2016目标是早睡早起作息规律按时吃饭'
        return render_template('test.jinja2', title=title)
