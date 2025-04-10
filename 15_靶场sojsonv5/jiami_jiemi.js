// 将sojson的代码进行本地替换，三板斧   先hook setInterval 再hook Function 最后hook toString
//将sojson的无限debugger处理掉之后剩下的就是的时间问题
var CryptoJS = require("crypto-js")


function fn(s){
    let _0x56f4e8 = '/sojson/api?page='+ s;
    let _0x335b45 = new Date()['getTime']();
    let _0x49f905 = CryptoJS['MD5']('duiduidui'+ _0x56f4e8+ 'taiduile'+ _0x335b45)['toString']();
    return {
        "Tm":_0x335b45,
        "Sign":_0x49f905,
    }
}

//测试代码
// ret = fn(1);
// console.log(ret);
