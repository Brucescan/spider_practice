import requests
import execjs

with open("youdao.js",'r',encoding='utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
form_data = js.call("encryptFn")
# print(type(params_headers))
# 第一步发请求，加密参数
form_data["i"] = "jay"
# print(form_data)

url = "https://dict.youdao.com/webtranslate"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-length": "313",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "OUTFOX_SEARCH_USER_ID=483827662@117.159.161.197; OUTFOX_SEARCH_USER_ID_NCOO=1237081216.901997; UM_distinctid=19604855d5413e-0094477ef121e-26001051-154ac4-19604855d55110c; _uetsid=81e7860012e611f0a4cdafb78c4b8d65; _uetvid=9e90e1d011e211f0abb0eda87f68e51c|52kwb|1743832573896|1|1|bat.bing.com/p/insights/c/b; DICT_DOCTRANS_SESSION_ID=ZWE1NjhlZDUtYjZmMS00MWIzLWEwNzItOTY2MTM2YmMwYTg5",
    "host": "dict.youdao.com",
    "origin": "https://fanyi.youdao.com",
    "referer": "https://fanyi.youdao.com/",
    "sec-ch-ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
# form_data=urlencode(form_data)
# print(form_data)
resp = requests.post(url, headers=headers, data=form_data)
# print(resp.text)
# 拿到数据后开始解密

res = js.call("decryptFn",resp.text)
print(res)


