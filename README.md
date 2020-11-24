# 郑大健康状况上报平台脚本

## ❗功能
使用Actions执行脚本，每天4点定时签到，无需手动运行。模拟手动操作，防止登录失效。

---
## ❓部署
### 1. Fork 仓库
   * 点击页面右上角的`Fork`按钮，将本项目保存到自己的仓库。
   <img src="">
### 2. 添加 secrets
   * 点击`Settings`-->`Secrets`-->`New repository secret`，进入新建页面。
   <img src="">
   * 在`Name`栏输入`UID`，`Value`栏输入自己的学号，然后点击`Add secret`。
   * 再次点击`Settings`-->`Secrets`-->`New repository secret`，进入新建页面。
   * 在`Name`栏输入`UPW`，`Value`栏输入自己的登录密码，然后点击`Add secret`。
### 3.启用 Actions
   * 点击上方的`Actions`，点击绿色按钮确认启用`Actions`功能。
   <img src="">
   * 点击左侧`Github Actions Clock Bot`，点击`Run workflow`，运行一次项目。
   <img src="">
---
项目部署完毕后，可以在`Actions`页面点击`zzu-commute-helper`-->`build`-->`Run sign`查看结果。如有疑问可通过`Issues`功能提交问题。
<img src="">
