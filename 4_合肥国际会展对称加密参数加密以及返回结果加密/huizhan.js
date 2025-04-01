var jt = {}
jt.a = require('crypto-js')
//加密函数
var sr = function(Xe) {
    Xe = JSON.stringify(Xe)
    var Zt = "$shanghaidianqi$"
    var Vt = "2023050814260000"
    var ot = jt.a.enc.Utf8.parse(Zt)
      , Kt = jt.a.enc.Utf8.parse(Vt)
      , kt = jt.a.AES.encrypt(Xe, ot, {
        iv: Kt,
        mode: jt.a.mode.CBC,
        padding: jt.a.pad.Pkcs7});
    return kt.toString()
}
//返回解密函数
mr = function(Xe) {
    var Zt = "$shanghaidianqi$"
    var Vt = "2023050814260000"
    var ot = jt.a.enc.Utf8.parse(Zt)
      , Kt = jt.a.enc.Utf8.parse(Vt)
      , kt = jt.a.AES.decrypt(Xe, ot, {
        iv: Kt,
        mode: jt.a.mode.CBC,
        padding: jt.a.pad.Pkcs7
    })
      , yr = kt.toString(jt.a.enc.Utf8);
    return yr.toString()
}
