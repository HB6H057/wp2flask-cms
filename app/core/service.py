#encoding: utf-8
from app.core.models import User, Post, Category, Tag, Comment

post_keys = [
    "id",
    "title",
    "slug",
    "body",
]

post_special_keys = [
    "timestamp",
    "tags",
]

cate_keys = [
    "id",
    "name",
    "slug",
    "description",
]

cate_special_keys = [
    "post_count",
]

comment_keys = [
    "id",
    "author",
    "email",
    "site",
    "content",
]

comment_special_keys = [
    "timestamp",
]

tag_keys = [
    "id",
    "name",
    "slug",
]

tag_special_keys = [
    "post_count",
]

class BaseService:
    def data_dict_list_generator(self, data=[], keys=[], skeys=[]):
        data_dict_list = []

        for d in data:

            data_dict = {}
            for k in keys:
                data_dict[k] = getattr(d, k, None)
            for sk in skeys:
                if sk == "post_count":
                    data_dict[sk] = d.posts.count()
                elif sk == "timestamp":
                    data_dict[sk] = d.timestamp.strftime("%F %H:%M:%S")
                elif sk == "tags":
                    data_dict[sk] = [ t.name for t in d.tags ]

            data_dict_list.append(data_dict)

        return data_dict_list

class PostService(BaseService):

    def get_post_list(self):
        posts = Post.query.all()

        post_dict_list = self.data_dict_list_generator(
                posts,
                post_keys,
                post_special_keys
            )

        return post_dict_list

    def get_post_by_pid(self, pid):
        p = Post.query.get(pid)

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

    def get_cate_of_post(self, pid):
        post = Post.query.get(pid)

        cate_dict = dict(
          id=post.category.id,
          name=post.category.name,
          slug=post.category.slug,
          post_count=post.category.posts.count(),
          description=post.category.description
        )

        return cate_dict

    def get_tags_of_post(self, pid):
        post = Post.query.get(pid)

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

    def get_comments_of_post(self, pid):
        post = Post.query.get(pid)

        comment_dict_list = [
            dict(
                id=cm.id,
                author=cm.author,
                email=cm.email,
                site=cm.site,
                content=cm.content,
                # timestamp="2016-03-13 05:57",
            )
        ]


class CategoryService(BaseService):
    def get_cate_list(self):
        cates = Category.query.all()

        cate_dict_list = self.data_dict_list_generator(
                cates,
                cate_keys,
                cate_special_keys
            )

        return cate_dict_list

    def get_cate_by_cid(self, cid):
        pass

    def get_posts_by_cid(self, cid):
        pass

class CommentService(BaseService):
    def get_comment_list(self):
        comments = Comment.query.all()

        comment_dict_list = self.data_dict_list_generator(
            comments,
            comment_keys,
            comment_special_keys
        )

        return comment_dict_list

    def get_comment_by_cmid(self, cmid):
        pass

    def get_post_by_cmid(self, cmid):
        pass

class TagService(BaseService):
    def get_tag_list(self):
        tags = Tag.query.all()

        tag_dict_list = self.data_dict_list_generator(
            tags,
            tag_keys,
            tag_special_keys
        )

        return tag_dict_list

    def get_tag_by_tid(self, tid):
        pass

    def get_posts_by_tid(self, tid):
        pass
