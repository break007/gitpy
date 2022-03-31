'''
Author: your name
Date: 2022-03-31 15:27:34
LastEditTime: 2022-03-31 17:09:33
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \gitpy\main.py
'''

import os
from time import sleep
import requests
import json
import urllib3
email = os.environ.get("email")
passwd = os.environ.get("passwd")
s = requests.session()
urllib3.disable_warnings()


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
    "authority":
    "ggok.xyz"
}

ran=4

def login():
    for i in range(ran):
        sleep(1)
        try:
            res = s.post("https://q88q.cyou/auth/login",
                         data={
                             "email": email,
                             "passwd": passwd
                         },
                         headers=headers,
                         verify=False)
            data = json.loads(res.content)
            print(data)
            break
        except Exception as e:
            print(e)
            print("登录异常，正在尝试第{}次:{}".format(i + 1, e))


def check_in():
    for i in range(ran):
        sleep(1)
        try:
            res = s.post("https://q88q.cyou/user/checkin",
                         data=None,
                         headers=headers,
                         verify=False)
            data = json.loads(res.content)
            print(data)
            break
        except Exception as e:
            print(e)
            print("签到，正在尝试第{}次:{}".format(i + 1, e))


login()
check_in()
