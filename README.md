# ❗功能
每天凌晨4点签到。在其他地方登录健康平台不影响脚本执行。学号密码保存在账号内，不会被复制。

**已知问题：表单隐藏内容可能以天为周期变化，具体情况有待观察。**

---
# ❓部署
## 1. Fork 仓库
   * 点击页面右上角的`Fork`，将本项目复制到自己的仓库。点击`Fork`左侧的`Star`可以表示对项目和作者的认同。
   ![fork.PNG](https://i.loli.net/2020/11/24/2hTtGldiZF9B7DX.png)
## 2. 添加 secrets
   * 点击`Settings`-->`Secrets`-->`New repository secret`，进入新建页面。
   ![secrets.PNG](https://i.loli.net/2020/11/24/mIWLRTzUJxuiMHa.png)
   * 在`Name`栏输入`UID`，`Value`栏输入自己的学号，然后点击`Add secret`。
   * 再次点击`Settings`-->`Secrets`-->`New repository secret`，进入新建页面。
   * 在`Name`栏输入`UPW`，`Value`栏输入自己的登录密码，然后点击`Add secret`。
   * 多人模式与单人模式的添加方法相同，具体格式为`学号,学号,学号`和`密码,密码,密码`，例如：`201884160000,201884160001`和`12345678,12345678`(**注意：逗号为英文标点，使用中文标点会导致脚本运行失败**)。
## 3.启用 Actions
   * 点击上方的`Actions`，点击绿色按钮确认启用Actions。
   * (推荐操作，可跳过)点击左侧`ZZU COMMUTE HELPER`，点击`Run workflow`，运行一次项目。
   ![actions.PNG](https://i.loli.net/2020/11/24/HrQoCwFkgcAYjps.png)
   * 所有运行结果可以在`Actions`页面点击`View workflow file`查看结果。
   ![check.PNG](https://i.loli.net/2020/11/24/GUEgdrmpIAxlPW5.png)
如有疑问可通过`Issues`功能提交，出现签到失败可能为打卡内容发生变化，请耐心等待更新。
**注意：项目启用后60天无更新时，Actions功能会自动关闭，届时需要再次手动开启。**

---
# 📢更新方法
   * 方法一:点击`Settings`-->`Options`-->`Dangerous Zone`-->`delete this reposity`，按照提示删除本项目，然后重新部署。
   * 方法二:使用git指令
   
