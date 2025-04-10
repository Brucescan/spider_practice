var CryptoJS = require("crypto-js")

function fn(s){
    let I1iI1I = '/sojson/api_3?page='+ s,
        illll1 = new Date()['getTime'](),
        IIIIl1 = CryptoJS['MD5']('zuihouyigela'+ I1iI1I+ 'zhenhao'+ illll1)['toString']();
    return {
        "Tm":illll1,
        "Sign":IIIIl1,
    }
}



//测试代码
// ret =  fn(2);
// console.log(ret);