# Devtools Project Config And Settings

这个文件用于开发者工具项目配置、常用设置和日常调试工作流。

## Scope

- `project.config.json`
- 项目设置
- 编译预览
- 自定义编译
- 调试面板
- 工具设置

## Typical Workflow

1. 先看项目基本信息和项目设置
2. 再看 `project.config.json` 与本地配置是否一致
3. 编译失败时区分工具问题和业务代码问题
4. 调试时按 `Console`、`Network`、`Storage`、`Sources`、模拟器面板逐层排查

## Working Rules

- 工具问题不要直接归因到业务代码
- 同一项目多人协作时，先统一工具配置和项目设置
- 需要解释构建行为时，先看项目配置页和调试页
- 发布配置和日常调试配置要区分，不要混写成一个问题

## Official Links

- 项目配置  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/project.html
- 配置文件  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/projectconfig.html
- 设置  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/settings.html
- 调试  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/debug.html
- 工具页面结构  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/page.html
