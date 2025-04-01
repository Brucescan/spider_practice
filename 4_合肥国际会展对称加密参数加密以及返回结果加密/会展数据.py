import requests
import execjs
import json
# 请求相关准备
url = "https://www.hfhuizhan.com/prod-api/hfhz-exhibition/back/exhibition/listExhibitionNotPage"
headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "null",
    "content-length": "55",
    "content-type": "application/json;charset=UTF-8, application/json;charset=UTF-8",
    "origin": "https://www.hfhuizhan.com",
    "priority": "u=1, i",
    "referer": "https://www.hfhuizhan.com/schedule",
    "sec-ch-ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
requests_data = {
    "yyyyMM": "2025-03",
}

#加密参数
with open('huizhan.js','r',encoding='utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
data = js.call('sr',requests_data)
# print(type(data))
form_data = {
    'data':data
}

resp = requests.post(url, headers=headers,data=json.dumps(form_data,separators=(',',':')))
# print(resp.text)
# 返回值解密
result = js.call('mr',resp.text)
print(result)