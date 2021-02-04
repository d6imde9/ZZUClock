# 郑大健康状况上报平台脚本

## ❗功能
使用Actions执行脚本，每天4点定时签到，无需手动运行。模拟手动操作，防止登录失效。
关于安全性：学号和密码用Secrect进行保存，复制项目到自己到账号下不会导致任何人的密码泄露。
**注意：项目启用后60天无更新时，Actions功能会自动关闭，届时需要再次手动开启。**

---
## ✨更新记录
1.24：表单内容更新，部分固定内容移动至myvs.txt中。

---
## ❓部署
### 1. Fork 仓库
   * 点击页面右上角的`Fork`按钮，将本项目保存到自己的仓库。点击`Fork`左侧的`Star`键可以表示您对本项目和作者的认同。
   ![fork.PNG](https://i.loli.net/2020/11/24/2hTtGldiZF9B7DX.png)
### 2. 添加 secrets
   * 点击`Settings`-->`Secrets`-->`New repository secret`，进入新建页面。
   ![secrets.PNG](https://i.loli.net/2020/11/24/mIWLRTzUJxuiMHa.png)
   * 在`Name`栏输入`UID`，`Value`栏输入自己的学号，然后点击`Add secret`。
   * 再次点击`Settings`-->`Secrets`-->`New repository secret`，进入新建页面。
   * 在`Name`栏输入`UPW`，`Value`栏输入自己的登录密码，然后点击`Add secret`。
### 3.启用 Actions
   * 点击上方的`Actions`，点击绿色按钮确认启用`Actions`功能。
   * 点击左侧`ZZU COMMUTE HELPER`，点击`Run workflow`，运行一次项目。
   ![actions.PNG](https://i.loli.net/2020/11/24/HrQoCwFkgcAYjps.png)

项目部署完毕后，可以在`Actions`页面点击`View workflow file`查看结果。
![check.PNG](https://i.loli.net/2020/11/24/GUEgdrmpIAxlPW5.png)
如有疑问可通过`Issues`功能提交问题，如出现签到失败的问题请耐心等待更新。

---
## 📢更新方法
   * 点击`Settings`-->`Options`-->`Dangerous Zone`-->`delete this reposity`，按照提示删除本项目，然后重新部署。
   * 如有意使用git，请自行搜索相关命令。
   

