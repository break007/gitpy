import json
import requests


class Notify:
    def send(self, content):
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        data = {
            "msgtype": "text",
            "text": {
                "content": content
            }
        }
        res = requests.post("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c4de16aa-91a8-496b-ae54-2c5d48bdc86d",
                            data=json.dumps(data), headers=headers)
        print(res.content)
