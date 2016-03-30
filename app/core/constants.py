#!/usr/bin/python
# encoding: utf-8

# ##
CAGE_PER_PAGE = 12
TAG_PER_PAGE = 12
HOME_HOT_POSTS_NUM = 11
# ## Post PageService Constants ##
# Post dict key
POST_DICT_KEY = [
    "id",
    "title",
    "slug",
    "cslug",
    "create_date",
]

# post page dict key
POST_PAGE_DICT_KEY = [
    "body",
]
POST_PAGE_DICT_KEY.extend(POST_DICT_KEY)

# post brief dict key
POST_BRIEF_DICT_KEY = [
    "brief",
]
POST_BRIEF_DICT_KEY.extend(POST_DICT_KEY)

# ## Tag PageService Constants ##
TAG_DICT_KEY = [
    "id",
    "name",
    "slug",
    "post_count",
]

# tag widget dict key
TAG_WIDGET_DICT_KEY = [
    "font_size",
]
TAG_WIDGET_DICT_KEY.extend(TAG_DICT_KEY)

# posts of cate page dict
TAG_PAGE_DICT_KEY = [
    "pagination",
]
TAG_PAGE_DICT_KEY.extend(TAG_DICT_KEY)

# ## Category PageService Constants ##
CATEGORY_DICT_KEY = [
    "id",
    "name",
    "slug",
    "post_count",
]
# posts of cate page dict
CATEGORY_PAGE_DICT_KEY = [
    "pagination",
]
CATEGORY_PAGE_DICT_KEY.extend(CATEGORY_DICT_KEY)
