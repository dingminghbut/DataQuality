import requests
import json

webhook = "https://oapi.dingtalk.com/robot/send?access_token=YOUR_ACCESS_TOKEN"

url = webhook
data = {
    "msgtype": "text",
    "text": {"content": "Hello, World!"}
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url=url, data=json.dumps(data), headers=headers)
print(response.text)
