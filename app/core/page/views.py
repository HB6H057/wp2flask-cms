# encoding: utf-8
from app.core.base import *

from . import page

@page.route('/about', methods=['GET', 'POST'])
def about():
    """
    about page
    """
    return 'Yes, it really, really, really could happen'

@page.route('/jiaofushu', methods=['GET', 'POST'])
def jiaofushu():
    """
    jiaofushu page
    """
    return 'All goes round again'
