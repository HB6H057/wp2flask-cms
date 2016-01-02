from app.core.base import *

from . import category

class CategoryViews(BaseViews):
    @category.route('/category/{string:slug}', methods=['GET', 'POST'])
    def category(self):
        """
        Category default page
        """
        self.test()

    @category.route('/category/{string:slug}/page/{int:page}', methods=['GET', 'POST'])
    def category_pagination(self):
        """
        Category pagination
        """
        self.test()
