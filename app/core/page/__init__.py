from flask import Blueprint

page = Blueprint('page', __name__)

from . import views
