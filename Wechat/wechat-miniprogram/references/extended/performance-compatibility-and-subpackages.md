# Performance Compatibility And Subpackages

这个文件用于性能优化、基础库兼容和分包。

## Performance Focus

优先检查这些高频问题：

- 启动慢
- 首屏渲染慢
- `setData` 过大或过频
- 图片、字体、网络资源过重
- 页面跳转和返回卡顿
- 弱网体验差

## Compatibility Focus

- 是否有基础库版本限制
- 是否需要 `wx.canIUse`
- 是否存在机型或客户端差异

## Subpackage Focus

- 主包是否过大
- 是否适合拆普通分包
- 是否需要独立分包
- 是否需要分包预下载

## Working Rules

- 先用官方性能面板和诊断规则定位，不要先盲改代码
- 优先减少不必要的 `setData` 体积和次数
- 分包策略先从路径和入口关系设计，不要只看文件大小
- 兼容性方案要同时写“检测方式 + 降级路径”

## Official Links

- 性能入口  
  https://developers.weixin.qq.com/miniprogram/dev/framework/performance/
- 性能优化总览  
  https://developers.weixin.qq.com/miniprogram/dev/framework/performance/tips.html
- `setData` 优化  
  https://developers.weixin.qq.com/miniprogram/dev/framework/performance/tips/runtime_setData.html
- 兼容性  
  https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html
- 分包加载  
  https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages.html
- 独立分包  
  https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/independent.html
- 分包预下载  
  https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/preload.html
