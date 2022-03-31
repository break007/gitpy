'''
Author: your name
Date: 2022-03-31 15:27:34
LastEditTime: 2022-03-31 15:50:52
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \gitpy\main.py
'''

import os
from time import sleep
import requests
import json

email = os.environ.get("email")
passwd = os.environ.get("passwd")
s = requests.session()

headers = {
    "content-type":
    "application/x-www-form-urlencoded; charset=UTF-8",
    "origin":
    "https://ggok.xyz",
    "referer":
    "https://ggok.xyz/auth/login",
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    " Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46",
    "Connection":
    "keep-alive",
    "accept-language":
    "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    # "Cookie":"cf_clearance=j8wQ0hx97XKSP.2CIaVflu5f8sYA6h35k_KxiNpScmI-1648541841-0-150; uid=707752; email=344267112%40qq.com; key=1d0f52dbcb22dd167724a38f71d44723c5310f41a7cc1; ip=af6dbff282f3db3bfe384eeb16787877; expire_in=1651306713",
    "authority":
    "ggok.xyz"
}


def login():
    for i in range(5):
        sleep(1)
        try:
            res = s.post("https://ggok.xyz/auth/login",
                         data={
                             "email": email,
                             "passwd": passwd
                         },
                         headers=headers,
                         verify=False)
            print(res.content)
            data = json.loads(res.content)
            print(data)
            break
        except Exception as e:
            print(e)
            print("登录异常，正在尝试第{}次".format(i + 1))


login()
