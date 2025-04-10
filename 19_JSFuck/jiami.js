//只有加密


var fn = function(s){
    var msg = '/jsfuck/api?page='+s;
    return btoa(msg);
}


//测试代码
// ret = fn(1);
// console.log(ret);


