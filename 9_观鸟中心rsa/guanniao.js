var JSEncrypt = require('node-encrypt-js')
var crypto = require("crypto")
var Base64 = require("js-base64")
var CryptoJS = require("crypto-js")


function sort_ASCII(obj) {
    var arr = new Array;
    var num = 0;
    for (var i in obj) {
        arr[num] = i;
        num++
    }
    var sortArr = arr.sort();
    var sortObj = {};
    for (var i in sortArr) {
        sortObj[sortArr[i]] = obj[sortArr[i]]
    }
    return sortObj
}
function getUuid() {
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 32; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 16), 1)
    }
    s[14] = "4";
    s[19] = hexDigits.substr(s[19] & 3 | 8, 1);
    s[8] = s[13] = s[18] = s[23];
    var uuid = s.join("");
    return uuid
}

function dataTojson(data) {
    var arr = [];
    var res = {};
    arr = data.split("&");
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].indexOf("=") != -1) {
            var str = arr[i].split("=");
            if (str.length == 2) {
                res[str[0]] = str[1]
            } else {
                res[str[0]] = ""
            }
        } else {
            res[arr[i]] = ""
        }
    }
    return res
}


function my_md5(s){
    return crypto.createHash("md5").update(s).digest("hex")
}

//  加密请求头代码 请求加密(包括请求头以及参数加密)
function encryptHeaders(options){
    var paramPublicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCvxXa98E1uWXnBzXkS2yHUfnBM6n3PCwLdfIox03T91joBvjtoDqiQ5x3tTOfpHs3LtiqMMEafls6b0YWtgB1dse1W5m+FpeusVkCOkQxB4SZDH6tuerIknnmB/Hsq5wgEkIvO5Pff9biig6AyoAkdWpSek/1/B7zYIepYY0lxKQIDAQAB";
    var encrypt = new JSEncrypt;
    encrypt.setPublicKey(paramPublicKey);
    var timestamp = Date.parse(new Date);
    var requestId = getUuid();
    var data = JSON.stringify(sort_ASCII(dataTojson(options.data || "{}")));
    options.data = encrypt.encryptLong(data);
    var sign = my_md5(data + requestId + timestamp);
    return {
        "sign":sign,
        'requestId':requestId,
        "timestamp":timestamp,
        "urlParam":options.data,
    }
}

function getMapping(_0x509dcf) {
    var _0x2b7e20 = {};
    _0x2b7e20['LbQfg'] = "53536868555767547048526949655455";
    var _0x245e3d = _0x2b7e20;
    for (var _0x1b74b3 = '', _0x33c0cd = 0x0; _0x33c0cd < _0x509dcf['length']; _0x33c0cd += 0x2) {
        var _0x37cad4 = _0x509dcf["substring"](_0x33c0cd, _0x33c0cd + 0x2);
        _0x1b74b3 += String['fromCharCode'](_0x37cad4);
    }
    return _0x1b74b3;

}
function decryptFn(data) {
    var _0x3c6fa1 = CryptoJS['enc']['Utf8']['parse'](getMapping('6756696653534952657053656868665752665050485566485667545454484967'))
      , _0x3ec027 = CryptoJS['enc']['Utf8']['parse'](getMapping('53536868555767547048526949655455'));
    return CryptoJS['AES']['decrypt'](data, _0x3c6fa1, {
        'iv': _0x3ec027,
        'mode': CryptoJS['mode']['CBC'],
        'padding': CryptoJS['pad']['Pkcs7']
    })['toString'](CryptoJS['enc']['Utf8']);
}

//测试代码

// var res = encryptHeaders({
//     "data":"page=2&limit=20"
// })
// console.log(res)
// console.log(my_md5("123456"))

//测试解密代码
// var res = decryptFn('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')
//
// console.log(res)
