import requests
import execjs

with open("jiami.js",'r',encoding='utf-8') as f:
    js_code=f.read()
js = execjs.compile(js_code)


url = "http://120.53.92.179:12345/disable/api"
my_paramas = {
    "page":1,
}
resp = js.call("fn",my_paramas["page"])
my_headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "host": "120.53.92.179:12345",
    "origin": "http://120.53.92.179",
    "pragma": "no-cache",
    "proxy-connection": "keep-alive",
    "referer": "http://120.53.92.179/",
    "sign": resp["m5"],
    "tm": str(resp["date"]),
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

result = requests.get(url,params=my_paramas,headers=my_headers)
print(result.json())