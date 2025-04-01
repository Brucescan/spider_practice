//根据作用域特性
// 偷鸡直接将整个md5扣出来

function fn(e, t, n) {
        "use strict";
        function i(e, t) {
            return e << t | e >>> 32 - t
        }
        function o(e, t) {
            var n, i, o, r, a;
            return o = 2147483648 & e,
            r = 2147483648 & t,
            n = 1073741824 & e,
            i = 1073741824 & t,
            a = (1073741823 & e) + (1073741823 & t),
            n & i ? 2147483648 ^ a ^ o ^ r : n | i ? 1073741824 & a ? 3221225472 ^ a ^ o ^ r : 1073741824 ^ a ^ o ^ r : a ^ o ^ r
        }
        function r(e, t, n) {
            return e & t | ~e & n
        }
        function a(e, t, n) {
            return e & n | t & ~n
        }
        function s(e, t, n) {
            return e ^ t ^ n
        }
        function c(e, t, n) {
            return t ^ (e | ~n)
        }
        function u(e, t, n, a, s, c, u) {
            return e = o(e, o(o(r(t, n, a), s), u)),
            o(i(e, c), t)
        }
        function l(e, t, n, r, s, c, u) {
            return e = o(e, o(o(a(t, n, r), s), u)),
            o(i(e, c), t)
        }
        function d(e, t, n, r, a, c, u) {
            return e = o(e, o(o(s(t, n, r), a), u)),
            o(i(e, c), t)
        }
        function f(e, t, n, r, a, s, u) {
            return e = o(e, o(o(c(t, n, r), a), u)),
            o(i(e, s), t)
        }
        function p(e) {
            for (var t = void 0, n = e.length, i = n + 8, o = (i - i % 64) / 64, r = 16 * (o + 1), a = Array(r - 1), s = 0, c = 0; c < n; )
                t = (c - c % 4) / 4,
                s = c % 4 * 8,
                a[t] = a[t] | e.charCodeAt(c) << s,
                c++;
            return t = (c - c % 4) / 4,
            s = c % 4 * 8,
            a[t] = a[t] | 128 << s,
            a[r - 2] = n << 3,
            a[r - 1] = n >>> 29,
            a
        }
        function g(e) {
            var t = ""
              , n = ""
              , i = void 0
              , o = void 0;
            for (o = 0; o <= 3; o++)
                i = e >>> 8 * o & 255,
                n = "0" + i.toString(16),
                t += n.substr(n.length - 2, 2);
            return t
        }
        function y(e) {
            e = e.replace(/\r\n/g, "\n");
            for (var t = "", n = 0; n < e.length; n++) {
                var i = e.charCodeAt(n);
                i < 128 ? t += String.fromCharCode(i) : i > 127 && i < 2048 ? (t += String.fromCharCode(i >> 6 | 192),
                t += String.fromCharCode(63 & i | 128)) : (t += String.fromCharCode(i >> 12 | 224),
                t += String.fromCharCode(i >> 6 & 63 | 128),
                t += String.fromCharCode(63 & i | 128))
            }
            return t
        }
        function h(e) {
            var t = []
              , n = void 0
              , i = void 0
              , r = void 0
              , a = void 0
              , s = void 0
              , c = void 0
              , h = void 0
              , m = void 0
              , v = void 0
              , w = 7
              , x = 12
              , _ = 17
              , b = 22
              , C = 5
              , U = 9
              , S = 14
              , E = 20
              , A = 4
              , T = 11
              , k = 16
              , D = 23
              , O = 6
              , F = 10
              , I = 15
              , L = 21;
            for (e = y(e),
            t = p(e),
            c = 1732584193,
            h = 4023233417,
            m = 2562383102,
            v = 271733878,
            n = 0; n < t.length; n += 16)
                i = c,
                r = h,
                a = m,
                s = v,
                c = u(c, h, m, v, t[n + 0], w, 3614090360),
                v = u(v, c, h, m, t[n + 1], x, 3905402710),
                m = u(m, v, c, h, t[n + 2], _, 606105819),
                h = u(h, m, v, c, t[n + 3], b, 3250441966),
                c = u(c, h, m, v, t[n + 4], w, 4118548399),
                v = u(v, c, h, m, t[n + 5], x, 1200080426),
                m = u(m, v, c, h, t[n + 6], _, 2821735955),
                h = u(h, m, v, c, t[n + 7], b, 4249261313),
                c = u(c, h, m, v, t[n + 8], w, 1770035416),
                v = u(v, c, h, m, t[n + 9], x, 2336552879),
                m = u(m, v, c, h, t[n + 10], _, 4294925233),
                h = u(h, m, v, c, t[n + 11], b, 2304563134),
                c = u(c, h, m, v, t[n + 12], w, 1804603682),
                v = u(v, c, h, m, t[n + 13], x, 4254626195),
                m = u(m, v, c, h, t[n + 14], _, 2792965006),
                h = u(h, m, v, c, t[n + 15], b, 1236535329),
                c = l(c, h, m, v, t[n + 1], C, 4129170786),
                v = l(v, c, h, m, t[n + 6], U, 3225465664),
                m = l(m, v, c, h, t[n + 11], S, 643717713),
                h = l(h, m, v, c, t[n + 0], E, 3921069994),
                c = l(c, h, m, v, t[n + 5], C, 3593408605),
                v = l(v, c, h, m, t[n + 10], U, 38016083),
                m = l(m, v, c, h, t[n + 15], S, 3634488961),
                h = l(h, m, v, c, t[n + 4], E, 3889429448),
                c = l(c, h, m, v, t[n + 9], C, 568446438),
                v = l(v, c, h, m, t[n + 14], U, 3275163606),
                m = l(m, v, c, h, t[n + 3], S, 4107603335),
                h = l(h, m, v, c, t[n + 8], E, 1163531501),
                c = l(c, h, m, v, t[n + 13], C, 2850285829),
                v = l(v, c, h, m, t[n + 2], U, 4243563512),
                m = l(m, v, c, h, t[n + 7], S, 1735328473),
                h = l(h, m, v, c, t[n + 12], E, 2368359562),
                c = d(c, h, m, v, t[n + 5], A, 4294588738),
                v = d(v, c, h, m, t[n + 8], T, 2272392833),
                m = d(m, v, c, h, t[n + 11], k, 1839030562),
                h = d(h, m, v, c, t[n + 14], D, 4259657740),
                c = d(c, h, m, v, t[n + 1], A, 2763975236),
                v = d(v, c, h, m, t[n + 4], T, 1272893353),
                m = d(m, v, c, h, t[n + 7], k, 4139469664),
                h = d(h, m, v, c, t[n + 10], D, 3200236656),
                c = d(c, h, m, v, t[n + 13], A, 681279174),
                v = d(v, c, h, m, t[n + 0], T, 3936430074),
                m = d(m, v, c, h, t[n + 3], k, 3572445317),
                h = d(h, m, v, c, t[n + 6], D, 76029189),
                c = d(c, h, m, v, t[n + 9], A, 3654602809),
                v = d(v, c, h, m, t[n + 12], T, 3873151461),
                m = d(m, v, c, h, t[n + 15], k, 530742520),
                h = d(h, m, v, c, t[n + 2], D, 3299628645),
                c = f(c, h, m, v, t[n + 0], O, 4096336452),
                v = f(v, c, h, m, t[n + 7], F, 1126891415),
                m = f(m, v, c, h, t[n + 14], I, 2878612391),
                h = f(h, m, v, c, t[n + 5], L, 4237533241),
                c = f(c, h, m, v, t[n + 12], O, 1700485571),
                v = f(v, c, h, m, t[n + 3], F, 2399980690),
                m = f(m, v, c, h, t[n + 10], I, 4293915773),
                h = f(h, m, v, c, t[n + 1], L, 2240044497),
                c = f(c, h, m, v, t[n + 8], O, 1873313359),
                v = f(v, c, h, m, t[n + 15], F, 4264355552),
                m = f(m, v, c, h, t[n + 6], I, 2734768916),
                h = f(h, m, v, c, t[n + 13], L, 1309151649),
                c = f(c, h, m, v, t[n + 4], O, 4149444226),
                v = f(v, c, h, m, t[n + 11], F, 3174756917),
                m = f(m, v, c, h, t[n + 2], I, 718787259),
                h = f(h, m, v, c, t[n + 9], L, 3951481745),
                c = o(c, i),
                h = o(h, r),
                m = o(m, a),
                v = o(v, s);
            return (g(c) + g(h) + g(m) + g(v)).toLowerCase()
        }
        return h

    }

function r(e, t) {
    if (!e.headers || !e.headers["x-platform"])
        return t.cid;
    var n = t.headerEncryptKeys.find(function(t) {
        return t.name == e.headers["x-platform"]
    });
    return n ? n.value : "DB2560A6EBC65F37A0484295CD4EDD25"
}


function s(e, t) {
    e = JSON.parse(e)
    t = JSON.parse(t)
    var n = "";
    if ("headers" == e.encryptType) {
        var i = e.data ? JSON.stringify(e.data) : "{}"
          , o = r(e, t);
        n = "cid=" + t.cid + "&param=" + i + o + t.timestamp
    } else {
        var a = [];
        a.push("cid=" + t.cid),
        a.push("uid=" + t.uid),
        a.push("ver=" + t.ver),
        a.push("devid=" + (e.deviceId || "")),
        a.push("t=" + t.timestamp),
        a.push("key=" + t.paramsKey),
        n = a.join(";")
    }
    var h = fn()
    var s = h(n);
    return s
}


function ceshi(ming,ming2){
    return s(ming,ming2);
}

