# Worker Wasm And Runtime Env

这个文件用于 Worker、多线程、WASM 和运行环境差异。

## Scope

- Worker
- 非主线程计算
- `WXWebAssembly`
- 运行环境差异
- JS 能力边界

## Working Rules

- 先判断问题是否真的需要非主线程
- 高计算、复杂数据处理、音视频等场景再考虑 Worker 或 WASM
- 先确认运行环境和 JS 支持边界，再设计方案
- 普通页面交互卡顿先查渲染和 `setData`，不要直接上 Worker

## Official Links

- Worker  
  https://developers.weixin.qq.com/miniprogram/dev/framework/workers.html
- WXWebAssembly  
  https://developers.weixin.qq.com/miniprogram/dev/framework/performance/wasm.html
- 运行环境  
  https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/env.html
- JS 支持能力  
  https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/js-support.html
