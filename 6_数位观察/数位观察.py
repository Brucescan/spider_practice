import requests
import json
import execjs

# 请求得到密文
url = "https://app.swguancha.com/client/v1/cPublic/consumer/baseInfo"
headers = {
    "accept": "application/json, text/plain, */*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-length": "173",
    "content-type": "application/json;charset=UTF-8",
    "devicetype": "1",
    "host": "app.swguancha.com",
    "origin": "https://www.swguancha.com",
    "referer": "https://www.swguancha.com/",
    "sec-ch-ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
data = {
    "size": 16,
    "current": 1,
    "propertyCode":
        ["DISTRICT_PROP_GJ025_RJDQSCZZ",
         "DISTRICT_PROP_GJ117_NMSYGGQDCYYCLS",
        "DISTRICT_PROP_GJ001_NMHJRK"],
    "dimensionTime": "2019",
    "levelType": 2
}
resp = requests.post(url=url, headers=headers, data=json.dumps(data,separators=(',',':')))
# print(resp.text)
# 执行js代码
with open('shuwei.js','r',encoding='utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
resp = js.call('fn',resp.text)
# 打印成功
print(resp)