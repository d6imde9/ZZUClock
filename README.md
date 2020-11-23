#郑大健康状况上报平台脚本

## ❗功能
使用Actions执行脚本，每天4点定时签到，无需手动运行。完全模拟手动操作，防止登录失效。

---
## ❓部署
### 1. Fork 仓库
   * 点击右上角`Fork`到自己的账号下
### 2. 添加 secrets
   * 回到项目页面，依次点击`Settings`-->`Secrets`-->`New secret`
   * 建立名为`UID`的 secret，值为自己的学号，然后点击`Add secret`
   * 建立名为`UPW`的 secret，值为自己的登录密码，然后点击`Add secret`
### 3.启用 Actions
Actions 默认为关闭状态，Fork 之后需要手动执行一次，若成功运行其才会激活。返回项目主页面，点击上方的`Actions`，再点击左侧的`Github Actions Clock Bot`，再点击`Run workflow`

---
至此，本项目部署完毕，您可以在`Actions`页面点击`zzu-commute-helper`-->`build`-->`Run sign`查看结果。如果签到失败，你会收到一封来自GitHub，标题为`Run failed: zzu-commute-helper - master`的邮件。如有疑问可以通过Issues功能提交问题。
