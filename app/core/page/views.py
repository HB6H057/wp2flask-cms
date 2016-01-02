form app.core.base import *

from . import page

class PageViews(Baseviews):
    @home.route('/about', methods=['GET', 'POST'])
    def index(self):
        """
        About page
        """
        self.test()
