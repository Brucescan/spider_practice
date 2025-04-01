import requests
import execjs


url = "https://data-server.cbaleague.com/api/teams/29136/seasons/2023/players"
headers = {
    "accept": "application/json, text/plain, */*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "isencrypt": "encrypt",
    "origin": "https://www.cbaleague.com",
    "priority": "u=1, i",
    "referer": "https://www.cbaleague.com/",
    "sec-ch-ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}

resp = requests.get(url, headers=headers)
# print(resp.text)
with open('cba.js','r',encoding="utf-8") as f:
    js_code = f.read()
ret = execjs.compile(js_code).call("a5e",resp.text.strip("\""))
print(ret)
