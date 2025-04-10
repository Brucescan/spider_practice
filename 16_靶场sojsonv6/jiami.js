var CryptoJS = require("crypto-js")


function fn(s){
    let _0x516512 = '/sojson/api_2?page='+ s;
    let _0xae4b4a = new Date()['getTime']();
    let _0x530a46 = CryptoJS['MD5']('shuiya'+ _0x516512+ 'mahuateng'+ _0xae4b4a)['toString']();
    return {
        "Tm":_0xae4b4a,
        "Sign":_0x530a46,
    }
}


//测试代码
// var ret = fn(1);
// console.log(ret)