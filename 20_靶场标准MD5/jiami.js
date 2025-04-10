var Crypto = require("crypto")

function my_md5(s){
    return Crypto.createHash("md5").update(s).digest("hex")
}


function fn(page){
    var tm = Date.now();
    var sign = my_md5(tm+""+page+"ILOVELADYGAGA");
    return {
        "page": page,
        "m": sign + "|" + tm
    }
}