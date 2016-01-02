from app.core.base import *

from . import post

class PostViews(BaseViews):
    @post.route('/{string:category}/{string:slug}.html', methods=['GET', 'POST'])
    def post(self):
        """
        Post page
        """
        self.test()
