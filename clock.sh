#!/bin/bash
uid=201884160115
upw=09292517
#使用学号和密码获取ptopid和sid
curl -d "uid=$uid&upw=$upw&smbtn=健康状况上报平台&hh28=722" "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login" -o "udata.txt"
udata='cat udata.txt'
udata=${udata#*ptopid=}
udata=${udata%\"\}\}*}
ptopid="${udata%&*}" 
sid="${udata#*&}"
#进入身份确认界面
curl -d "did=1&men6=a&ptopid=$ptopid&sid=$sid" "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"
#进行打卡
url="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"
curl -d "myvs_1=否&myvs_2=否&myvs_3=否&myvs_4=否&Btn3=获取地市&myvs_13c=河南省.郑州市.金水区&myvs_14=否&did=2&day6=b&men6=a&ptopid=$ptopid&sid=$sid" url
