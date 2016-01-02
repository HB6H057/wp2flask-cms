from app.core.base import *

from . import home

class HomeViews(BaseViews):
    @home.route('/', methods=['GET', 'POST'])
    def index(self):
        """
        Index page
        """
        self.test()
