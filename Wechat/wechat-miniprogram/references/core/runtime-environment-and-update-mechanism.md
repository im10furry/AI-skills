# Runtime Environment And Update Mechanism

这个文件用于运行环境、热冷启动、JS 支持边界和更新机制。

## Runtime Model

- 小程序运行在特定客户端和基础库环境中
- 行为会受客户端版本、基础库版本和运行环境影响
- 生命周期文档负责页面和应用事件，本文件负责更底层的运行机制理解

## What To Check

- 冷启动和热启动区别
- 前后台切换
- 运行环境差异
- JS 支持边界
- 更新检测和更新应用流程

## Working Rules

- 行为异常先确认是不是运行环境或基础库差异
- 更新问题先查 `UpdateManager`，不要只看页面生命周期
- JS 语法和能力问题先查运行环境支持文档，不要默认浏览器环境

## Official Links

- 运行机制  
  https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/operating-mechanism.html
- 更新机制  
  https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/update-mechanism.html
- 运行环境  
  https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/env.html
- JS 支持能力  
  https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/js-support.html
- 更新管理器  
  https://developers.weixin.qq.com/miniprogram/dev/api/base/update/wx.getUpdateManager.html
