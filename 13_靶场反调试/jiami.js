var CryptoJS = require("crypto-js")
function fn(page){
    let url = '/disable/api?page='+page;
    let date = new Date().getTime();
    let m5 = CryptoJS.MD5("woai"+url+"hulatang"+date).toString()
    return {
        date,
        m5,
    }
}

var ret = fn();
console.log(ret)