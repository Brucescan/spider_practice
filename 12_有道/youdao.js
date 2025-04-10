var crypto = require("crypto")

function my_md5(s){
    return crypto.createHash("md5").update(s.toString()).digest("hex");
}

function encryptFn(){
    const a = (new Date).getTime();
    var t = "Vy4EQ1uwPkUoqvcP1nIu6WiAjxFeA3Y3"
    return {
        sign: my_md5(`client=fanyideskweb&mysticTime=${a}&product=webfanyi&key=${t}`),
        client: "fanyideskweb",
        product: "webfanyi",
        appVersion: "1.0.0",
        vendor: 'web',
        pointParam: 'client,mysticTime,product',
        mysticTime: a,
        keyfrom: 'fanyi.web',
        mid: 1,
        screen: 1,
        model: 1,
        network: 'wifi',
        abtest: 0,
        yduuid: "abcdefg",
        from: "auto",
        to: "",
        useTerm: false,
        dictResult: true,
        keyid: "webfanyi",

    }
}
function T(e) {
    return crypto.createHash("md5").update(e).digest()
}

function decodeData(e, t, a){
    const o = Buffer.alloc(16, T(t))
      , n = Buffer.alloc(16, T(a))
      , r = crypto.createDecipheriv("aes-128-cbc", o, n);
    let s = r.update(e, "base64", "utf-8");
    return s += r.final("utf-8"),
    s
}
function decryptFn(s){
    return decodeData(s, "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl", "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4");
}
//测试代码
// var res = encryptFn()
// console.log(res)


// var res = decryptFn("Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml6MdaC9LzSO4qdlPmtuyg_YvDQQMdLTVnTMYtInG0ZBrNPOPNzjjiq-jHBIXclo3bdhEzfuCQJrHD9t_lAkSsXJJMWMnE2HZm_g86NPlGORn2w21mrfqMP_Mc96pue4l-upHy_Dlw8NKfIiqjkfVSG6kxyE3oj-56b5O7rjrKZ1ddUeivB627dvhzgf1Q5iugT-mU2NUPmcPsbp6iVXQ24ol07NwF1jJZmICT4Jc4qv4dt5oxft01Fv6RKqUSspdQjl1ePM9YiH_1iKjo-LN5UnVOp3wvbZSKvNIBKC-Th1NLSPkSEYMTl3AfBb7TKDSw3HDpsfZSAs-I78hplaQdsUjfG9YiyYER_pWstmNdsnMzzUV7GSp6vp5Jh8BkYA6hjQr93DYTafwAeXml0PoFr3hM1GKC2HSoN-k40A06hKJ0P6I-dFnKyvn0MyEcoUh2ggzQLyd4FukFaKxQzQfaA5Z7ZByF-7jA5HCbwQeeJgUV4IY9iGyZ5xkYG_AlegcuXVGroLs21GWfY-SBaom7DUzkBTC38fotkVCfzd5gPsZofTr_ZmWmM_CIa4WLulYT5xsvKVUFpguspyPrcEXs6koZhny5ZCzbrIxhMJX7uyEF9rxwnIoYfoH4KTiZIUoSUju7N8Vo-APiKOoBkeCrSwfyDXNRKxDEN4Yg8afiW-QMP5LhdOWtLPgZZJDXpgU7jXV5wLLk8UA_eTKifbRI3OzxinwsV3l3xGZnnbS6NGZKfJrLGkdGjZVB9LZhECOMKD8OM-bnJRKKpI6-5juw1lDeTLyxewCx8aAF9BAW9JqZIVtMLw7wMKwVip27BbLmCUKT0oaWDK8DTos-_gIwkF5tCzphT8FQL2ysIO-Q92IZ8oRPYQzm9QlUNN_6vC-Y-HQN0-S8WPAHVri2tdmTy8_uZm5bzZ-oLQXNSZWItt6-f3NpKQvPOidJTTq8ody2eBXJa8ImoF1I4ZeX0quLMme7T4SsuMMI0pKCXETNU5ae30Vm818QSbt2yqZAZe7_OLE-gUgBtX0KgwTxMlaswrRkq4q76NvXY3Pz0uwzW24aTx_iH3gcXu6Nywdl5Jk20jDDYlozu74RyrJZYj3Xol1roY3LD8HqyqZUqbssKYHeFI7VNqi8dQ9SboWSC43J_Uv0exurLIXtEYFWuKp-TgKdXdYn1lPXIINwsPx2Ohpc=")
// console.log(res)