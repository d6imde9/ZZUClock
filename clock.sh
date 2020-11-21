#!/bin/bash

uid=201884160115 #替换为自己的学号
upw=09292517 #替换为自己的密码

#使用学号和密码获取ptopid和sid
curl -1 -d "uid=$uid&upw=$upw&smbtn=健康状况上报平台&hh28=722" "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login" -o "udata.txt"
udata=sed -n '11p' udata.txt
udata=${udata#*ptopid=}
udata=${udata%\"*}
ptopid="${udata%&*}" 
sid="${udata#*&}"

#进入身份确认界面
curl -1 -d "did=1&men6=a&ptopid=$ptopid&sid=$sid" "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"

#进行打卡
url="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid=${ptopid}&sid=${sid}"
curl -1 -d "ptopid=$ptopid&sid=$sid" url
