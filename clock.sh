#!/bin/bash


uid=201884160115 #替换为自己的学号
upw=09292517 #替换为自己的密码

curl -d "uid=$uid&upw=$upw&smbtn=健康状况上报平台&hh28=722" "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login" -o "udata.txt"

ptopid=grep "ptopid=.+&" udata.txt
sid=grep "sid=.+\"" udata.txt

curl -d "did=1&men6=a&ptopid=$ptopid&sid=$sid" "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"

url="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid=${ptopid}&sid=${sid}"

curl -d "ptopid=$ptopid&sid=$sid" url
