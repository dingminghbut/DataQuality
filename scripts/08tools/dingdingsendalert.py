# coding=utf-8
import datetime
import sys
import os
import requests
import json
# import pymysql

def dingmessage(self):
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=******"
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "msgtype": "text",   # 告警类型
        "text": {
            "content": self  # 告警文字内容
        },
        "at": {
            "atMobiles": [
                "18123808608", "18576753500"  # 手机号对应告警组里的人
            ],
            "isAtAll": False  # 此处为是否@所有人 True  所有人  False  无需所有人
        }
    }
    message_json = json.dumps(message)
    info = requests.post(url=webhook, data=message_json, headers=header)
    print('发送成功')
    print(info.json())
dingmessage("监控告警:  归集库 数据库监控到磁盘空间不够")

