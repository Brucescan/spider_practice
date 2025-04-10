import requests
import execjs

url = "https://api.qimai.cn/indexV2/getIndexRank"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "cookie": "synct=1743824266.839; syncd=-1560; qm_check=A1sdRUIQChtxen8pI0dAMRcOUFseEHBeQF0JTjVBWDAIXEQaYhAQbF1FIRUJCBETVkQSGAlIBAhVVlNeOU9TFXNbQlxTQAshV1ZIDgolAGgCEElDaw06VktIPEo+BAYbEhUSV1AABQxKQltKGQceABUAGAhHGw%3D%3D; PHPSESSID=jlp5hartu0gdqi8n33u8lmd6gk; gr_user_id=00808029-996e-4275-9e9b-64d3fd05d7bc; ada35577182650f1_gr_session_id=bedb3960-efdb-4988-a3d4-da483f724e16; ada35577182650f1_gr_session_id_sent_vst=bedb3960-efdb-4988-a3d4-da483f724e16",
    "host": "api.qimai.cn",
    "origin": "https://www.qimai.cn",
    "sec-ch-ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

with open("qimai.js", 'r', encoding='utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
data = {
    "params": {
        "setting": 0,
        "genre": "36",
    },
    "url": "/indexV2/getIndexRank",
    "baseURL": "https://api.qimai.cn",
}
res = js.call("encryptFn", data)
param = {
    "setting": 0,
    "genre": "36",
    "analysis": res["url"].split("=")[-1]
}

resp = requests.get(url, params=param, headers=headers)
print(resp.json())
