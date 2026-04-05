# DevTools Release And Compliance

这个文件用于开发者工具、调试、CI、上传发布和基础合规入口。

## DevTools

高频页面：

- 开发者工具总览
- 项目配置
- 调试面板
- 编译与预览
- 远程调试
- CLI / CI

## Release Flow

1. 本地编译通过
2. 真机预览
3. 需要团队协作时走版本管理
4. 上传代码
5. 提交审核
6. 发布上线
7. 观察运营数据和体验分

## Compliance Baseline

至少检查这些问题：

- 合法域名和 HTTPS
- 用户隐私保护和授权接入
- 健康运营要求
- 体验评分与基础审计项

## Working Rules

- 工具问题先回到 `devtools` 文档，不要把所有问题都当成业务代码问题
- 发布问题先区分“工具链报错”还是“平台审核规则”
- 隐私与审核规则优先看当前官方文档，不要复述过时结论

## Official Links

- 开发者工具  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/devtools
- 调试  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/debug.html
- 项目配置  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/project.html
- CLI  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/cli.html
- CI  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/ci.html
- 协同工作与发布  
  https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/release.html
- 域名  
  https://developers.weixin.qq.com/miniprogram/dev/framework/ability/domain.html
- 运营指引  
  https://developers.weixin.qq.com/miniprogram/dev/framework/operation.html
- 隐私保护  
  https://developers.weixin.qq.com/miniprogram/dev/framework/user-privacy/miniprogram-intro.html
