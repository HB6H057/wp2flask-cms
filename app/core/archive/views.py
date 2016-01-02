from app.core.base import *

from . import archive

class ArchiveViews(BaseViews):
    @archive.route('/archive/{int:year}/{int:month}', methods=['GET', 'POST'])
    def archive(self):
        """
        Archive default page
        """
        self.test()

    @archive.route('/archive/{int:year}/{int:month}/page/{int:page}', methods=['GET', 'POST'])
    def archive_pagination(self):
        """
        Archive pagination
        """
        self.test()
