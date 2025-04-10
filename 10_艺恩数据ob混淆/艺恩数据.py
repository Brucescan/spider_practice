import requests
import execjs

url = "https://www.endata.com.cn/API/GetData.ashx"

from_data = {
    "year": "2017",
    "MethodName": "BoxOffice_GetYearInfoData"
}
headers = {
    "accept": "text/plain, */*; q=0.01",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-length": "46",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "host": "www.endata.com.cn",
    "origin": "https://www.endata.com.cn",
    "sec-ch-ua": "Chromium;v=129, Not=A?Brand;v=8",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
resp = requests.post(url, headers=headers,data=from_data)
# print(resp.text)
# 拿到返回的密文后开始进行解密
with open("yien.js",'r',encoding="utf-8") as f:
    js_code = f.read()
js = execjs.compile(js_code)
data = js.call("shell",resp.text)
# print(base64.b64decode(data))
print(data)



