#encoding: utf-8
from app.core.models import User, Post, Category, Tag

class BaseService():
    def test():
        print 'test'

class PostService(BaseService):

    def get_post_list(self):
        posts = Post.query.all()

        post_dict_list = [
            dict(
                id=p.id,
                title=p.title,
                slug=p.slug,
                body=p.body,
                # timestamp
                tags=[
                    t.name
                    for t in p.tags
                ],
            )
            for p in posts
        ]

        return post_dict_list

    def get_post_by_pid(self, id):
        p = Post.query.get(id)

        post_dict = dict(
            id=p.id,
            title=p.title,
            slug=p.slug,
            body=p.body,
            # timestamp
            tags=[
                t.name
                for t in p.tags
            ]
        )

        return post_dict

    def get_cate_of_post(self, id):
        post = Post.query.get(id)

        cate_dict = dict(
          id=post.category.id,
          name=post.category.name,
          slug=post.category.slug,
          post_count=post.category.posts.count(),
          description=post.category.description
        )

        return cate_dict

    def get_tags_of_post(self, id):
        post = Post.query.get(id)

        tag_dict_list = [
          dict(
            id=t.id,
            name=t.name,
            slug=t.slug,
            post_count=t.posts.count()
          )
          for t in post.tags
        ]

        return tag_dict_list


class CategoryService(BaseService):
    def get_cate_list(self, cid):
        pass

    def get_cate_by_cid(self, cid):
        pass

    def get_posts_by_cid(self, cid):
        pass

class CommentService(BaseService):
    def get_comment_list(self):
        pass

    def get_comment_by_cmid(self, cmid):
        pass

    def get_post_by_cmid(self, cmid):
        pass

class TagService(BaseService):
    def get_tag_list(self):
        pass

    def get_tag_by_tid(self, tid):
        pass

    def get_posts_by_tid(self, tid):
        pass
