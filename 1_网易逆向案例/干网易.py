import requests
import json
import execjs
url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=5dcf3c20e46d6b0e3ad8f9e1d0235a03"
headers = {
    "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "502",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "NMTID=00OIzx83ENQ3Dt3TUsykY71CvgDas4AAAGVxkjKew; _iuqxldmzr_=32; _ntes_nnid=c7f8b8fc5c9d535cb9c02c9628effb43,1742788415411; _ntes_nuid=c7f8b8fc5c9d535cb9c02c9628effb43; WEVNSM=1.0.0; WNMCID=gzkgrw.1742788418725.01.0; WM_TID=fnXG7yG5ZdNERRUQUAPCIqV9IcGjofC2; sDeviceId=YD-zTh7qJJJt6VEEkFUUQeWM%2FU4MJWzt%2Bhi; ntes_utid=tid._.GcWooC44oqNAE0BAUQOCM6E5McHjp%252B03._.0; __snaker__id=OVas7M7aLSQfx1MA; ntes_kaola_ad=1; WM_NI=w27xmGsG2G7ARC76KfULPeK0HQpIZlzt%2FrIF6IpOyMEyegZqrPJVut5BthmkBY4MRjBl7sP7D27jVKHkMIZGTOILskAgWh0mffE0tWOfbqrcVYX6c%2B92z5f9xgY2sKNheDM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee99ef4283a797aed74ab7e78aa7d45e968a8f82db46b3868dd8e872908c9a98d82af0fea7c3b92ab5eef999f04db199fea8b64b929df9d7ca6e9794a086ca3c8c8fc0aad968baace193cc4ef697c0b0fc4787a7ab88d97bb29086b7f880f79ebc89f0618287fcaed16282b4f994d33d88eef98bd5418cb583aad94d989187adf26183b99989b367a6ba8bd1f75d8dbaae92f169968798d7e221fbeeb6d6e533bcb997d3f2418eb8aba5d037e2a3; gdxidpyhxdE=CH2hmTu0M20ZcdVG3WH5NbbEgdfnEHQt5Uil36kX3RX%2B0%5CtkQ7a3wwbh4CT3R9qKxQ3yofWe4UvR2D6ODtHWReH3LGM7J0KXVql7ELTHzRA4gH88dDP6jcx9ymRi0YbWMTbmkxjArso4AbD%2FlvTNafqG7J9XtenDqH%2FhR64mbyVccWlt%3A1742984811823; P_INFO=18739878035|1742983989|1|music|00&99|null&null&null#SG&null#10#0|&0|null|18739878035; __csrf=5dcf3c20e46d6b0e3ad8f9e1d0235a03; MUSIC_U=0039DFB5F41EBB90DE6B09D68022DE5A76C9C712B3894BDBBAE10C920C0555EEF21E53EE238D55DC48FFA9703DBD6CF583F5873E3605313504A1EF77417E4DC7C94AFE737EFEE9DEBA02CA35EE92D1AF163AECF8D5724F1DDA45CC073634A18A9F8216632400B13FA25434FB8FF5D7E4925129E0A533C13CD4A681C619427209B7A000588CC07E6C72E6CC9E63076624DE1EBFDB28102358DB4280C3C5C0A0CE150346C1D9804BFFBC92E42D0C9E4BC67DDCEC243DC772EB68D85B7E35F7A64BA18C34135E085BD6172CD6C020967BEC840CB56DBDDF270B1A9E3C05313E8D3B58AF63180239F24E9864D406F461453F452C2E60B5D95611438F33D163DCCCC77DF93B20C7BB3CA87895A23AA420DF9ED64CF23719F59D1AFE04D166C000F5793421E4723AF58BFFA0043B6DFB77D096A4050A33E3237B1EB543731032090DDBEDA3A76C797D346A874FF16ED6CC8E92324FB18F7DBC9EB7BBD5B3B99FB50D7F22; __remember_me=true; JSESSIONID-WYYY=m5vZV95XrnhBOwfc0Rz8zWy8qR4O40RmW9TS1nFN43XJ44EV4ODfDJK16XIdI9qizHYJ5g5XnWiQF%5CMr8CCAtghzarUpIBACIUzUaF6WxE9dPKsug1Ecv5QWTZ1iVNbTf5cxnc4ZardubFO2TMzs%2FYfSix%2BoDMbqWFAXzCY%2Bp9PwdJHg%3A1743048882761",
    "origin": "https://music.163.com",
    "priority": "u=1, i",
    "referer": "https://music.163.com/",
    "sec-ch-ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

# 获取网易js代码
f = open("扣网易js.js",'r',encoding="utf-8")
js_code = f.read()
f.close()

# 执行js代码获得逆向参数
js = execjs.compile(js_code) # 加载js代码
data = {
    "csrf_token": "5dcf3c20e46d6b0e3ad8f9e1d0235a03",
    "encodeType": "aac",
    "ids": "[28577876]",
    "level": "standard"
}
ret = js.call("fn",json.dumps(data,separators=(",",":")))
print(ret)

# 发送请求
form_data  = {
    "params":ret["encText"],
    "encSecKey":ret["encSecKey"],
}
resp = requests.post(url=url,headers=headers,data=form_data)
print(resp.text)