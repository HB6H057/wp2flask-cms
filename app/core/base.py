# encoding: utf-8
from flask import render_template

from app.core.models import User, Post

class BaseSerive(object):
    @staticmethod
    def random_get_data(self, model=Post, count=3):
        """
        Random get data (no finish)
        """
        return model.query.limit(count).all()
