import requests
import execjs


url  = "https://api.birdreport.cn/front/activity/search"
jiami_data = {
    "data":"page=2&limit=20",
}

with open("guanniao.js",'r',encoding='utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
resp = js.call("encryptHeaders",jiami_data)
# print(resp)
# print(type(resp))
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-length": "172",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "host": "api.birdreport.cn",
    "origin": "https://www.birdreport.cn",
    "referer": "https://www.birdreport.cn/",
    "requestid": resp["requestId"],
    "sec-ch-ua": "Chromium;v=129, Not=A?Brand;v=8",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sign": resp["sign"],
    # "sign": "A7FE736373403219F79ED764F8BF8111",
    "timestamp": str(resp["timestamp"]),
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

data_resp = requests.post(url,headers = headers,data = resp["urlParam"])
# print(base64.b64decode(data_resp.json()['data']))

# 拿到加密的返回数据后开始解密
data_res = js.call("decryptFn",data_resp.json()['data'])
print(data_res)

