import requests
import execjs

url = "http://120.53.92.179:12345/sojson/api_3"
params = {
    "page":"2",
}
with open("jiami.js",'r',encoding='utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
res = js.call("fn",params["page"])

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
    "Sign": res["Sign"],
    "Tm": str(res["Tm"]),
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}


resp = requests.get(url,headers=my_headers,params=params)
print(resp.json())