# 整体逻辑   先请求public得到公钥 -> 接下来对调用js对明文参数加密 -> 加密完发送请求
import json
import requests
import execjs

pub_url = "https://ec.minmetals.com.cn/open/homepage/public"
resp = requests.post(pub_url, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"})
# print(resp.text)


# 拿到公钥后进行加密
with open("wukuang.js", "r", encoding="utf-8") as f:
    js_code = f.read()
js = execjs.compile(js_code)
data = {
    "businessClassfication": "100",
    "dwmc": "",
    "inviteMethod": "",
    "lx": "ZBGG",
    "mc": "",
    "pageIndex": 1
}
res = js.call("fn", data,resp.text)
data_url = "https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-length": "696",
    "content-type": "application/json",
    "cookie": "__jsluid_s=b4a3ed37b1b67091197b0160cacf9d63; SUNWAY-ESCM-COOKIE=be9fe0da-ce9b-4cfa-8187-b486f1ad7234; JSESSIONID=35536EE0D6F79B28835F6BABB9D82DFB",
    "host": "ec.minmetals.com.cn",
    "origin": "https://ec.minmetals.com.cn",
    "referer": "https://ec.minmetals.com.cn/open/home/purchase-info?tabIndex=0",
    "sec-ch-ua": "Chromium;v=129, Not=A?Brand;v=8",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

resp = requests.post(data_url, headers=headers, data=res)
print(resp.text)
