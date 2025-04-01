//两种找到加密入口的逻辑，因为是服务器加密返回数据，所以找到send后找onreadystatechange这个函数之后往下找加密入口
//2、第二种方案，看到axios，可以直接试着找一下interceptors，可以秒杀
var Fv = require("crypto-js")

//这就是cba的解密函数
function a5e(e) {
    const t = "uVayqL4ONKjFbVzQ";
    var r = Fv.enc.Utf8.parse(t)
      , n = Fv.AES.decrypt(e, r, {
        mode: Fv.mode.ECB,
        padding: Fv.pad.Pkcs7
    });
    return JSON.parse(Fv.enc.Utf8.stringify(n))
}
