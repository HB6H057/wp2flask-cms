from flask import Blueprint

archive = Blueprint('archive', __name__)

from . import views
