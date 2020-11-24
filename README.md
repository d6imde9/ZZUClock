# 郑大健康状况上报平台脚本

## ❗功能
使用Actions执行脚本，每天4点定时签到，无需手动运行。模拟手动操作，防止登录失效。

---
## ❓部署
### 1. Fork 仓库
   * 点击页面右上角的`Fork`按钮，将本项目保存到自己的仓库。~~点击`Fork`左侧的`Star`按钮可以表示您对本项目和作者的认同。~~
   ![fork.PNG](https://i.loli.net/2020/11/24/jZnibqcVXrmlWts.png)
### 2. 添加 secrets
   * 点击`Settings`-->`Secrets`-->`New repository secret`，进入新建页面。
   ![secrets.PNG](https://i.loli.net/2020/11/24/mIWLRTzUJxuiMHa.png)
   * 在`Name`栏输入`UID`，`Value`栏输入自己的学号，然后点击`Add secret`。
   * 再次点击`Settings`-->`Secrets`-->`New repository secret`，进入新建页面。
   * 在`Name`栏输入`UPW`，`Value`栏输入自己的登录密码，然后点击`Add secret`。
### 3.启用 Actions
   * 点击上方的`Actions`，点击绿色按钮确认启用`Actions`功能。
   <img src="">
   * 点击左侧`Github Actions Clock Bot`，点击`Run workflow`，运行一次项目。
   ![actions.PNG](https://i.loli.net/2020/11/24/HrQoCwFkgcAYjps.png)
---
项目部署完毕后，可以在`Actions`页面点击`View workflow file`查看结果。
![check.PNG](https://i.loli.net/2020/11/24/GUEgdrmpIAxlPW5.png)
如有疑问可通过`Issues`功能提交问题，如出现签到失败的问题请耐心等待更新。

