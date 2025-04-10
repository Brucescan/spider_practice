var CryptoJS = require("crypto-js")


var fn_jiami =function (s){
    let url = '/aaencode/api?page='+s;
    let m5 = CryptoJS.MD5('qiaofu'+url).toString()
    return {
        "Sign":m5,
    }
}


var fn_jiemi = function(s){
    let key = "00000apecome.com";
    let iv = '0102030405060708';
    let key_bs = CryptoJS.enc.Utf8.parse(key);
    let iv_bs = CryptoJS.enc.Utf8.parse(iv);
    let result = CryptoJS.AES.decrypt(s, key_bs, {
        iv:iv_bs,
        mode:CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return JSON.parse(result.toString(CryptoJS.enc.Utf8))
}