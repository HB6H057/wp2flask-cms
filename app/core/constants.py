#!/usr/bin/python
# encoding: utf-8

# ##
CAGE_PER_PAGE = 6
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

# ## ListPageService Constants ##
LIST_PAGE_DICT_KEY = [
    "id",
    "name",
    "slug",
    "post_count",
    "pagination",
]

# ## Comment PageService Constants ##
COMMENT_DICT_KEY = [
    "id",
    "author",
    "email",
    "site",
    "content",
    "create_date",
    "post_id"
]

HTML = u'''
<tbody>
<tr>
<td width="127" valign="top"><strong>核心知识</strong></td>
<td colspan="2" width="441" valign="top"><strong>课标解读</strong><strong>&nbsp;</strong></td>
</tr>
<tr>
<td rowspan="4" width="127" valign="top">力的概念</td>
<td width="36" valign="top">1</td>
<td width="405" valign="top">理解力是物体之间的相互作用，能找出施力物体和受力物体．</td>
</tr>
<tr>
<td width="36" valign="top">2</td>
<td width="405" valign="top">知道力的作用效果．</td>
</tr>
<tr>
<td width="36" valign="top">3</td>
<td width="405" valign="top">知道力有大小和方向，会画出力的图示或力的示意图．</td>
</tr>
<tr>
<td width="36" valign="top">4</td>
<td width="405" valign="top">知道力的分类．</td>
</tr>
<tr>
<td rowspan="3" width="127" valign="top">重力的确概念</td>
<td width="36" valign="top">5</td>
<td width="405" valign="top">知道重力是地面附近的物体由于受到地球的吸引而产生的．</td>
</tr>
<tr>
<td width="36" valign="top">6</td>
<td width="405" valign="top">知道重力的大小和方向，会用公式<em>Ｇ＝ｍｇ</em>计算重力．</td>
</tr>
<tr>
<td width="36" valign="top">7</td>
<td width="405" valign="top">知道重心的概念以及均匀物体重心的位置．</td>
</tr>
<tr>
<td rowspan="3" width="127" valign="top">弹力的概念</td>
<td width="36" valign="top">8</td>
<td width="405" valign="top">知道什么是弹力以及弹力产生的条件．</td>
</tr>
<tr>
<td width="36" valign="top">9</td>
<td width="405" valign="top">能在力的图示（或力的示意图）中正确画出弹力的方向．</td>
</tr>
<tr>
<td width="36" valign="top">10</td>
<td width="405" valign="top">知道如何显示微小形变．</td>
</tr>
<tr>
<td rowspan="3" width="127" valign="top">胡克定律</td>
<td width="36" valign="top">11</td>
<td width="405" valign="top">知道在各种形变中，形变越大，弹力越大．</td>
</tr>
<tr>
<td width="36" valign="top">12</td>
<td width="405" valign="top">知道胡克定律的内容和适用条件．</td>
</tr>
<tr>
<td width="36" valign="top">13</td>
<td width="405" valign="top">对一根弹簧，会用公式<em>ｆ＝ｋｘ</em>进行计算．</td>
</tr>
<tr>
<td rowspan="4" width="127" valign="top">摩擦力的概念</td>
<td width="36" valign="top">14</td>
<td width="405" valign="top">知道滑动摩擦力产生的条件，会判断滑动摩擦力的方向．</td>
</tr>
<tr>
<td width="36" valign="top">15</td>
<td width="405" valign="top">会利用公式<em>ｆ＝μＮ</em>进行计算，知道动摩擦因数跟什么有关</td>
</tr>
<tr>
<td width="36" valign="top">16</td>
<td width="405" valign="top">知道静摩擦产生的条件，会判断静摩擦力的方向．</td>
</tr>
<tr>
<td width="36" valign="top">17</td>
<td width="405" valign="top">知道最大静摩擦力跟两物间的压力成正比</td>
</tr>
<tr>
<td rowspan="2" width="127" valign="top">二力平衡</td>
<td width="36" valign="top">18</td>
<td width="405" valign="top">知道什么是力的平衡．</td>
</tr>
<tr>
<td width="36" valign="top">19</td>
<td width="405" valign="top">知道二力平衡的条件．</td>
</tr>
<tr>
<td rowspan="7" width="127" valign="top">力的合成和分解</td>
<td width="36" valign="top">20</td>
<td width="405" valign="top">理解力的合成和合力的概念．</td>
</tr>
<tr>
<td width="36" valign="top">21</td>
<td width="405" valign="top">理解力的合成和合力的概念．</td>
</tr>
<tr>
<td width="36" valign="top">22</td>
<td width="405" valign="top">掌握平行四边形定则，会用作图法、公式法求合力的大小和方向．</td>
</tr>
<tr>
<td width="36" valign="top">23</td>
<td width="405" valign="top">熟悉力的三角形法．</td>
</tr>
<tr>
<td width="36" valign="top">24</td>
<td width="405" valign="top">掌握平行四边形定则．</td>
</tr>
<tr>
<td width="36" valign="top">25</td>
<td width="405" valign="top">理解力的分解和分力的概念．理解力的分解是力的合成逆运算，</td>
</tr>
<tr>
<td width="36" valign="top">26</td>
<td width="405" valign="top">会用作图法求分力，会用直角三角形的知识计算分力</td>
</tr>
<tr>
<td rowspan="2" width="127" valign="top">矢量和标量及运算</td>
<td width="36" valign="top">27</td>
<td width="405" valign="top">知道什么是矢量，什么是标量．</td>
</tr>
<tr>
<td width="36" valign="top">28</td>
<td width="405" valign="top">知道平行四边形定则是矢量加法运算的普遍定则．</td>
</tr>
<tr>
<td width="127" valign="top">受力分析</td>
<td width="36" valign="top">2</td>
<td width="405" valign="top">初步熟悉物体的受力分析．</td>
</tr>
</tbody>
'''
