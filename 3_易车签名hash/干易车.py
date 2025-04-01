import time
import requests
import json
import execjs

url = "https://mapi.yiche.com/web_app/api/v1/city/get_near_citys_by_city_id?cid=508&param=%7B%22cityId%22%3A%22201%22%2C%22size%22%3A4%7D"
# 计算头中的sign值
with open('模拟易车.js','r',encoding='utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
timestamp = str(int(time.time()*1000))
ming1 = {
    "encryptType":"headers",
    "data":{
        "cityId":"201",
        "serialId":"1661"
    }
}
ming2 = {
    "cid":"508",
    "uid":"",
    "ver":"v10.80.0",
    "paramsKey":"f48aa2d0-31e0-42a6-a7a0-64ba148262f0",
    "timestamp": timestamp,
}
sign = js.call('ceshi',json.dumps(ming1,separators=(',',':')),json.dumps(ming2,separators=(',',':')))
# print(sign)

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cid": "508",
    "content-type": "application/json;charset=UTF-8",
    "cookie": "CIGUID=ed92ec3de490ab5e0a3b56d8769db0d7; auto_id=5625c618da663b79a8b052d725e2231e; selectcity=110100; selectcityid=201; selectcityName=%E5%8C%97%E4%BA%AC; selectcityPinyin=beijing; UserGuid=ed92ec3de490ab5e0a3b56d8769db0d7; isWebP=true; locatecity=110100; bitauto_ipregion=123.5.2.207%3A%E6%B2%B3%E5%8D%97%E7%9C%81%E7%84%A6%E4%BD%9C%E5%B8%82%3B201%2C%E5%8C%97%E4%BA%AC%2Cbeijing; Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1743070783,1743337617; Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44=1743337617; HMACCOUNT=14A87D4378EB91FF",
    "origin": "https://car.yiche.com",
    "priority": "u=1, i",
    "referer": "https://car.yiche.com/siyucivic/peizhi/",
    "reqid": "3bd8c55d5a79852cba2b44999ebfcfec",
    "sec-ch-ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "x-city-id": "201",
    "x-ip-address": "123.5.2.207",
    "x-platform": "pc",
    "x-sign": sign,
    "x-timestamp": timestamp,
    "x-user-guid": "ed92ec3de490ab5e0a3b56d8769db0d7"
}

resp = requests.get(url,headers=headers)
print(resp.text)
