# 首先是登录的逻辑
# 先获取验证码图片 -> 识别验证码 —> 请求服务器请求得到时间 ->接下来对登录请求参数进行加密 -> 发送登录请求登录成功 -> 请求头再次设置获取数据
# 案例网址
import json
import requests
import base64
from ddddocr import DdddOcr
import execjs

session = requests.session()
# 首先要加载界面
url = "https://user.wangxiao.cn/login"
resp = session.get(url)
# print(resp.text)

captcha_url = "https://user.wangxiao.cn/apis//common/getImageCaptcha"
captcha_resp = session.post(captcha_url,headers={
    "content-type": "application/json;charset=UTF-8"
})
# 得到验证码
image = captcha_resp.json()['data'].split(',')[-1]
# 识别验证码
docr = DdddOcr(show_ad=False)
captcha_res = docr.classification(base64.b64decode(image))
print(captcha_res)
# 发送请求服务器时间
time_url = "https://user.wangxiao.cn/apis//common/getTime"
time_resp = session.post(time_url,headers={"content-type":"application/json;charset=UTF-8"})
time = time_resp.json()['data']
print(time)
with open("wangxiao.js","r",encoding="utf-8") as f:
    js_code = f.read()
js = execjs.compile(js_code)
password = "1233455jing040216"
pws = js.call("encryptFn",password+str(time))
# print(type(pws))
# 对登录请求参数进行加密并发送请求
data = {
    "imageCaptchaCode": captcha_res,
    "userName": "18739878035",
    "password": pws
}

login_url = "https://user.wangxiao.cn/apis//login/passwordLogin"
login_resp = session.post(login_url,headers={
    "content-type":"application/json;charset=UTF-8"
},data=json.dumps(data,separators=(',',':')))
print(login_resp.text)

data_url = "https://ks.wangxiao.cn/practice/listQuestions"

session.cookies['autoLogin'] = "null"
session.cookies['userInfo'] = json.dumps(login_resp.json()['data'])
session.cookies['token'] = json.dumps(login_resp.json()['data']['token'])
session.cookies["UserCookieName"] = json.dumps(login_resp.json()['data']['userName'])
session.cookies['OldUsername2'] = json.dumps(login_resp.json()['data']['userNameCookies'])
session.cookies['OldUsername'] = json.dumps(login_resp.json()['data']['userNameCookies'])
session.cookies['OldPassword'] = json.dumps(login_resp.json()['data']['passwordCookies'])
session.cookies['UserCookieName_'] = json.dumps(login_resp.json()['data']['userName'])
session.cookies['OldUsername2_'] = json.dumps(login_resp.json()['data']['userNameCookies'])
session.cookies['OldUsername_'] = json.dumps(login_resp.json()['data']['userNameCookies'])
session.cookies['OldPassword_'] = json.dumps(login_resp.json()['data']['passwordCookies'])

# 验证码登录之后开始爬取数据，
payload_data = {
    "practiceType":"1",
    "sign":"jzs1",
    "subsign":"5166078fbf1eed222fe9",
    "day":"20250402"
}
data_resp = session.post(data_url,headers ={
    "content-type":"application/json; charset=UTF-8"
},data=json.dumps(payload_data,separators=(',',':')))
print(data_resp.text)







