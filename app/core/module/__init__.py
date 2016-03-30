from flask import Blueprint

module = Blueprint('module', __name__,
                   static_folder='static',
                   template_folder='templates',)

from . import views
