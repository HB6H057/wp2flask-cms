# encoding: utf-8
from app.core.base import *

from . import home

@home.route('/')
def index():
    """
    Index page
    """
    return 'first templates'
