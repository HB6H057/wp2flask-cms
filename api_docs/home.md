### 主页
- URL: '/'
- method: 'GET'

```js
{
  "success": true,
  "data":{
    "hot_list":[
      {
          "title": "标题1",
          "cate_slug": "shuxue",
          "slug": "test"
      },{
          "title": "标题2",
          "cate_slug": "yuwen",
          "slug": "test2"
      }
      //共11条......
    ],
    "random_brief":[
      {
          "title": "标题",
          "brief": "这是一段简短的描述。",
          "cate_slug": "shuxue",
          "slug": "test"
      },
      {
          "title": "标题2",
          "brief": "这是一段简短的描述。",
          "cate_slug": "shuxue",
          "slug": "test2"
      }
      //随机3条......
    ],
    "cate_list":[
      {
        "cate_name": "数学",
        "cate_slug": "shuxue",
        "post_list":[
          {
            "title": "标题1",
            "slug": "test"
          },
          {
            "title": "标题2",
            "slug": "test2"
          },
          //最新5条
        ]
      },
      {
        "cate_name": "语文",
        "cate_slug": "yuwen",
        "post_list":[
          {
            "title": "标题1",
            "slug": "test"
          },
          {
            "title": "标题2",
            "slug": "test2"
          },
          //最新5条
        ]
      }
      //根据目录数量而定......
    ]
  }
}
```
