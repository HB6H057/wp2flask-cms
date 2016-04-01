from flask import Blueprint

home = Blueprint('apiv1', __name__)

from . import views
