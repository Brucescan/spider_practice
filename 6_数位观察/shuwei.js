var u = require("crypto-js")

function fn(data){
    var l = "QV1f3nHn2qm7i3xrj3Y9K9imDdGTjTu9"
    var n = u.enc.Utf8.parse(l)
      , r = u.AES.decrypt(data, n, {
        mode: u.mode.ECB,
        padding: u.pad.Pkcs7
    })
      , i = r.toString(u.enc.Utf8);
    return i;
}