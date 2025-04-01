import requests
import execjs
import base64
import json
session = requests.session()

# 识别验证码
url_verify_img = "https://www.jisilu.cn/account/captcha/4181"
verify_img_headers = {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "kbz_newcookie=1; kbzw__Session=lfv9qnq06idjqbkh032csm8rn7; Hm_lvt_164fe01b1433a19b507595a43bf58262=1743323599; HMACCOUNT=E4E7373AB9631057; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1743324553",
    "priority": "i",
    "referer": "https://www.jisilu.cn/account/login/",
    "sec-ch-ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
resp = session.get(url_verify_img,headers=verify_img_headers)
# print(resp.content)
with open("验证码.png",'wb') as f:
    f.write(resp.content)
# 验证码认证的逻辑
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        #！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""

img_path = "验证码.png"
result = base64_api(uname='brucescan', pwd='Jing040216', img=img_path, typeid=3)
print(result)


url_verify = "https://www.jisilu.cn/webapi/account/check_code_verify/"
data ={
"code_verify": result
}
verify_headers = {
    "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "18",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "kbz_newcookie=1; kbzw__Session=lfv9qnq06idjqbkh032csm8rn7; Hm_lvt_164fe01b1433a19b507595a43bf58262=1743323599; HMACCOUNT=E4E7373AB9631057; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1743324553",
    "origin": "https://www.jisilu.cn",
    "priority": "u=1, i",
    "referer": "https://www.jisilu.cn/account/login/",
    "sec-ch-ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
resp = session.post(url_verify,headers=verify_img_headers,data=data)
print(resp.text)

# 登录的逻辑
url = "https://www.jisilu.cn/webapi/account/login_process/"
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "145",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "kbz_newcookie=1; kbzw__Session=lfv9qnq06idjqbkh032csm8rn7; Hm_lvt_164fe01b1433a19b507595a43bf58262=1743323599; HMACCOUNT=E4E7373AB9631057; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1743323603",
    "origin": "https://www.jisilu.cn",
    "priority": "u=1, i",
    "referer": "https://www.jisilu.cn/account/login/",
    "sec-ch-ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
# 执行js加密我们的登录参数
with open('jisilu.js','r',encoding='utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
user_name = js.call('jslencode','aksjdkajsd')
password = js.call('jslencode','ahsjdasd')
form_data = {
    "return_url": "https%3A%2F%2Fwww.jisilu.cn%2F",
    "user_name": user_name,
    "password": password,
    "aes": "1",
    "auto_login": "0",
    "code_verify": result,
}
resp = session.post(url,headers=headers,data=form_data)
print(resp.text)