# 郑大健康状况上报平台脚本

## ❗功能
使用Actions执行脚本，每天4点定时签到，无需手动运行。模拟手动操作，防止登录失效。

---
## ❓部署
### 1. Fork 仓库

   * 点击页面右上角的`Fork`按钮，将本项目保存到自己的仓库。
### 2. 添加 secrets
   * 点击`Settings`-->`Secrets`-->`New repository secret`，进入新建页面。
   * 在`Name`栏输入`UID`，`Value`栏输入自己的学号，然后点击`Add secret`。
   * 再次点击`Settings`-->`Secrets`-->`New repository secret`，进入新建页面。
   * 在`Name`栏输入`UPW`，`Value`栏输入自己的登录密码，然后点击`Add secret`。
### 3.启用 Actions
Actions 默认为关闭状态，Fork 之后需要手动执行一次，若成功运行其才会激活。返回项目主页面，点击上方的`Actions`，再点击左侧的`Github Actions Clock Bot`，再点击`Run workflow`

---
项目部署完毕后，您可以在`Actions`页面点击`zzu-commute-helper`-->`build`-->`Run sign`查看结果。如有疑问可以通过Issues功能提交问题。
