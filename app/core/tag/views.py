form app.core.base import *

from . import tag

class TagViews(Base)
    @home.route('/tag/{string:slug}', methods=['GET', 'POST'])
    def tag(self):
        """
        Tag default page
        """
        self.test()

    @home.route('/tag/{string:slug}/page/{int:page}', methods=['GET', 'POST'])
    def tag_pagination(self):
        """
        Tag pagination
        """
        self.test()
