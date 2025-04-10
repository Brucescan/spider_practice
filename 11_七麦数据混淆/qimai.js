
function fn_o(n) {
    t = '';
    ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function(n) {
        t += unescape('%u00' + n)
    });
    var t, e = t;
    return String[e](n)
}
function fn_h(n, t) {
    t = t || 'a12c0fa6ab9119bc90e4ac7700796a53';
    for (var e = (n = n['split'](''))['length'], r = t['length'], a = 'charCodeAt', i = 0; i < e; i++)
        n[i] = fn_o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n['join']('')
}
function fn_p(t) {
    t = encodeURIComponent(t)['replace'](/%([0-9A-F]{2})/g, function(n, t) {
        return fn_o('0x' + t)
    });
    return btoa(t)

}
function encryptFn(t) {
    var n;
    var s=1560;
    var e, r = +new Date - s  - 1661224081041, a = [];
    return undefined === t['params'] && (t['params'] = {}),
    Object['keys'](t['params'])['forEach'](function(n) {
        if (undefined == 'analysis')
            return false;
        t['params']['hasOwnProperty'](n) && a["push"](t['params'][n])
    }),
    a = a["sort"]()['join'](''),
    a = fn_p(a),
    a = (a += '@#' + t['url']['replace'](t['baseURL'], '')) + ('@#' + r) + ('@#' + 3),
    e = fn_p(fn_h(a, 'xyz517cda96efgh')),
    -1 == t['url']['indexOf']('analysis') && (t['url'] += (-1 != t["url"]['indexOf']('?') ? '&' : "?") + 'analysis' + '=' + encodeURIComponent(e)),
    t
}
//测试代码
// var test_data  ={
//     "params":{
//         "setting":0,
//         "genre": "36",
//     },
//     "url":"/indexV2/getIndexRank",
//     "baseURL":"https://api.qimai.cn",
// }
// var res = encryptFn(test_data)
// console.log(res)