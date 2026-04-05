# Runtime Routing And Lifecycle

这个文件用于逻辑层运行机制、生命周期、页面栈和更新机制。

## Runtime Baseline

- 小程序存在逻辑层和渲染层
- 生命周期问题先区分是 `App`、`Page` 还是组件
- 路由问题先区分是普通页面、`tabBar` 页面还是重启型跳转

## Common App Lifecycle

- `onLaunch`
- `onShow`
- `onHide`
- `onError`
- `onPageNotFound`
- `onUnhandledRejection`

## Common Page Lifecycle

- `onLoad`
- `onShow`
- `onReady`
- `onHide`
- `onUnload`

常见页面事件：

- `onPullDownRefresh`
- `onReachBottom`
- `onShareAppMessage`
- `onPageScroll`
- `onTabItemTap`

## Route APIs

- `wx.navigateTo`
- `wx.redirectTo`
- `wx.switchTab`
- `wx.reLaunch`
- `wx.navigateBack`

## Working Rules

- 普通页面间跳转优先用 `navigateTo` 或 `redirectTo`
- 目标是 `tabBar` 页面时用 `switchTab`
- 要清空路由栈时用 `reLaunch`
- 不要在复杂逻辑里滥用 `getCurrentPages()`

## Scene And Update

- 场景值读取：
  - `wx.getLaunchOptionsSync()`
  - `wx.getEnterOptionsSync()`
- 版本更新：
  - `wx.getUpdateManager()`

## Official Links

- App Service  
  https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/
- 页面生命周期  
  https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page-life-cycle.html
- 页面路由  
  https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route.html
- 场景值  
  https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/scene.html
- 运行机制  
  https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/operating-mechanism.html
- 更新机制  
  https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/update-mechanism.html
