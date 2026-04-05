# Minimal Tabbar And Subpackage Config

```json
{
  "pages": [
    "pages/index/index"
  ],
  "tabBar": {
    "list": [
      {
        "pagePath": "pages/index/index",
        "text": "首页"
      }
    ]
  },
  "subpackages": [
    {
      "root": "packageA",
      "pages": [
        "pages/detail/index"
      ]
    }
  ]
}
```

规则：

- 主包放首屏和公共高频路径
- 分包放低频、重资源或业务隔离模块
- 分包策略要和路由设计一起考虑

官方链接：

- https://developers.weixin.qq.com/miniprogram/dev/framework/config.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages.html
