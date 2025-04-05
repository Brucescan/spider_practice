var JSEncrypt = require("node-encrypt-js")

function encryptFn(e) {
    var o = new JSEncrypt;
    return o.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"),
    o.encrypt(e)
}


//测试
// var encryptFn1 = encryptFn("12334551743515359522");
// console.log(encryptFn1)