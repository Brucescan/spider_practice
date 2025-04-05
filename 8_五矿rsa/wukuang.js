var JSEncrypt = require("node-encrypt-js")
var crypto = require("crypto")

function my_md5(s){
    return crypto.createHash("md5").update(s).digest("hex")
}
function fn(e,r){
    var t = new JSEncrypt();
    t.setPublicKey(r);
    e.sign=my_md5(JSON.stringify(e));
    e.timeStamp = +new Date;
    var s = t.encryptLong(JSON.stringify(e));
    return JSON.stringify({
        "param":s,
    })
}

//测试
// data = {
//     "businessClassfication": "100",
//     "dwmc": "",
//     "inviteMethod": "",
//     "lx": "ZBGG",
//     "mc": "",
//     "pageIndex": "1"
// }
// var res = fn(data,"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCN+ghqCZXnFwmHbtFwFevOEpzq6evVdua/ze6CqgSPOSwPkcsCti5lnr6lhBR0pKZ2QqqJXxCwmq1iheVBuHLALSvlW1puK8KRJiQMcb5NbsAK40Tjh6Zaq+zrUGP/UhfKvpDgIxO6Z3fajTQ+cfaMBy4V0l67EybgplGdaHeDRwIDAQAB");
// console.log(res)
