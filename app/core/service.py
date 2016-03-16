#encoding: utf-8
from sqlalchemy import func
from app.core.models import User, Post, Category, Tag, Comment

post_keys = [
    "id",
    "title",
    "slug",
    "body",
    "category_id",
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
    def data_dict_generator(self, d, keys=[], skeys=[]):
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

        return data_dict

    def data_dict_list_generator(self, data=[], keys=[], skeys=[]):
        data_dict_list = []

        for d in data:
            data_dict = self.data_dict_generator(d, keys, skeys)
            data_dict_list.append(data_dict)

        return data_dict_list

class PostService(BaseService):

    def get_post_list(self, kw=[]):
        base_query = Post.query

        if kw is not None and isinstance(kw, dict):
            if 'cid' in kw.keys() and kw['cid'] is not None:
                base_query = base_query.filter_by(category_id=kw['cid'])
            if 'tid' in kw.keys() and kw['tid'] is not None:
                base_query = base_query.filter_by(category_id=kw['cid'])
            if 'random' in kw.keys() and kw['random'] == 'true':
                base_query = base_query.order_by(func.random())
            if 'limit' in kw.keys() and kw['limit'] is not None:
                base_query = base_query.limit(kw['limit'])

        posts = base_query.all()

        post_dict_list = self.data_dict_list_generator(
                posts,
                post_keys,
                post_special_keys
            )

        return post_dict_list

    def get_post_by_pid(self, pid):
        p = Post.query.get(pid)

        post_dict = self.data_dict_generator(
            p,
            post_keys,
            post_special_keys,
        )

        return post_dict

    def get_cate_of_post(self, pid):
        post = Post.query.get(pid)

        cate_dict = self.data_dict_generator(
            post.category,
            cate_keys,
            cate_special_keys
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

        comment_dict_list = self.data_dict_list_generator(
            post.comments,
            comment_keys,
            comment_special_keys
        )

        return comment_dict_list

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
        cate = Category.query.get(cid)

        cate_dict = self.data_dict_generator(
            cate,
            cate_keys,
            cate_special_keys
        )

        return cate_dict

    def get_posts_by_cid(self, cid):
        cate = Category.query.get(cid)

        post_dict_list = self.data_dict_list_generator(
            cate.posts,
            post_keys,
            post_special_keys
        )

        return post_dict_list

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
        comment = Comment.query.get(cmid)

        comment_dict = self.data_dict_generator(
            comment,
            comment_keys,
            comment_special_keys
        )

        return comment_dict

    def get_post_by_cmid(self, cmid):
        comment = Comment.query.get(cmid)

        post_dict = self.data_dict_generator(
            comment.post,
            post_keys,
            post_special_keys
        )

        return post_dict


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
        tag = Tag.query.get(tid)

        tag_dict = self.data_dict_generator(
            tag,
            tag_keys,
            tag_special_keys
        )

        return tag_dict

    def get_posts_by_tid(self, tid):
        tag = Tag.query.get(tid)

        post_dict_list = self.data_dict_list_generator(
            tag.posts,
            post_keys,
            post_special_keys
        )

        return post_dict_list
