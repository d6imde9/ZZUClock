#!/bin/bash

uid=$1
upw=$2
smbtn=进入健康状况上报平台

#获取ptopid和sid
curl -d "uid=${uid}&upw=${upw}&smbtn=${smbtn}&hh28=722" "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login" -o temp.txt
udata=$(sed -n '11p' temp.txt)
udata=${udata#*ptopid=}
udata=${udata%\"\}\}*}
ptopid="${udata%&*}"
sid="${udata#*&sid=}"
url="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"

#进入身份确认界面
curl -d "day6=b&did=1&men6=a&ptopid=${ptopid}&sid=${sid}" ${url}
#进行打卡

myvs_13c=河南省.郑州市.金水区
curl -d "myvs_1=否&myvs_2=否&myvs_3=否&myvs_4=否&Btn3=获取地市&myvs_13a=41&myvs_13b=4101&myvs_13c=${myvs_13c}&myvs_14=否&ptopid=${ptopid}&sid={$sid}" ${url}
