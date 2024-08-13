
function sig(L) {
    for (var N = 0, g = encodeURIComponent(L), B = 0; B < g["length"]; B++)
        N = ((((N << 7) - N) + 398) + g["charCodeAt"](B)),
        N |= 0;
    return N;
}
function de(L, N) {
    var g = L["FW"] + L["hash"];
    g += N,
    N = (((((sig(g) + '|') + 0) + '|') + new Date()["getTime"]()) + '|1'),
    g = ua(N, true),
    N = {};
    N["type__1286"] = g,
    L["search"] = H['Fa'](L["search"], N);
    return H['FY'](L);
}

function ua(E, H) {

    var W = ["3", "4", "2", "1", "0"]
      , P = 0;
    while (!![]) {
        switch (W[P++]) {
        case '0':
            switch (M["length"] % 4) {
            default:
            case 0:
                return M;
            case 1:
                return (M + "===");
            case 2:
                return (M + '==');
            case 3:
                return (M + '=');
            }
            continue;
        case '1':
            if (H)
                return M;
            continue;
        case '2':
            var M = uu(E, 6, function(L) {
                return string.charAt(L);
            });
            continue;
        case '3':
            var K = {};
            K["uGGDj"] = "DGi0YA7BemWnQjCl4+bR3f8SKIF9tUz/xhr2oEOgPpac=61ZqwTudLkM5vHyNXsVJ";
            var V = K;
            continue;
        case '4':
            if (null === E)
                return '';
            continue;
        }
        break;
    }
}
function uu(E, H, W) {
                    var az = F3;
                    if (F[az(lw.F)](null, E))
                        return '';
                    for (var P, M, K, V, L = {}, N = {}, B = '', Q = 0xf * -0x175 + -0x1ee * 0xe + 0x30e1, R = -0x26e * 0x8 + -0x100e + 0x2381, I = -0x1f7a + 0x1f44 + 0x38, T = [], w = -0x1d46 + 0x1dd5 + -0x8f * 0x1, k = -0x1249 * -0x1 + -0x1a7d + 0x3c * 0x23, v = -0x25b * -0xe + 0x1 * -0x105d + 0x109d * -0x1; F[az(lw.Y)](v, E[az(lw.U)]); v += -0x147 * -0x12 + 0x1789 + -0x2e86)
                        if (K = E[az(lw.a)](v),
                        Object[az(lw.A)][az(lw.D) + az(lw.o)][az(lw.i)](L, K) || (L[K] = R++,
                        N[K] = !(0x1031 + -0x260 * -0xb + -0x2a51)),
                        V = F[az(lw.y)](B, K),
                        Object[az(lw.G)][az(lw.S) + az(lw.m)][az(lw.l)](L, V))
                            B = V;
                        else {
                            if (Object[az(lw.E)][az(lw.H) + az(lw.o)][az(lw.i)](N, B)) {
                                if (F[az(lw.W)](B[az(lw.P)](0x1 * 0x6f3 + 0x1 * 0x1d9e + -0x2491), 0x5 * 0x25f + 0x21b1 + -0x2c8c)) {
                                    for (P = -0x7a1 * -0x2 + -0x1c4f * -0x1 + -0x2b91; F[az(lw.M)](P, I); P++)
                                        w <<= -0x1f87 + 0x1 * -0x1585 + -0x350d * -0x1,
                                        F[az(lw.K)](k, F[az(lw.V)](H, -0x1c4 * 0x10 + 0xc50 + -0x35 * -0x4d)) ? (k = -0xca * -0xa + 0x1736 + -0x1f1a,
                                        T[az(lw.L)](F[az(lw.N)](W, w)),
                                        w = -0x9a4 + -0x1 * -0x11f1 + -0x11 * 0x7d) : k++;
                                    for (M = B[az(lw.P)](0x16d * -0xd + -0x28d * 0x3 + -0x8 * -0x346),
                                    P = -0xa9 * 0x10 + 0x3ce * 0x5 + -0x876; F[az(lw.g)](P, -0x2 * -0xce3 + 0x5 * -0x726 + 0xa00); P++)
                                        w = F[az(lw.B)](F[az(lw.Q)](w, -0x347 * -0x7 + -0xd * 0x1f7 + 0x1d * 0x17), F[az(lw.R)](-0x1cea + -0x1 * -0xec9 + 0xc9 * 0x12, M)),
                                        F[az(lw.f)](k, F[az(lw.u)](H, 0x2b2 + 0x1737 + -0x19e8)) ? (k = -0x21c + 0x17 * -0x135 + 0x1 * 0x1ddf,
                                        T[az(lw.I)](F[az(lw.T)](W, w)),
                                        w = -0x2171 + -0x11c2 + -0x1111 * -0x3) : k++,
                                        M >>= 0x2 * -0x27c + 0x2496 + 0x1f9d * -0x1;
                                } else {
                                    for (M = -0x1190 * -0x1 + -0x125 + 0x835 * -0x2,
                                    P = 0x1 * 0x2fb + -0x1 * 0x166f + 0x1374; F[az(lw.w)](P, I); P++)
                                        w = F[az(lw.k)](F[az(lw.p)](w, -0x78e * -0x5 + 0x10 * 0x11 + -0x26d5), M),
                                        F[az(lw.v)](k, F[az(lw.X)](H, -0x123f * 0x1 + -0x1e9 * -0x1 + 0x1 * 0x1057)) ? (k = -0x273 + 0x1ff6 * -0x1 + 0x2269,
                                        T[az(lw.L)](F[az(lw.C)](W, w)),
                                        w = -0x1 * -0x2335 + 0x1 * 0x1f96 + 0x42cb * -0x1) : k++,
                                        M = -0x2638 + -0x1 * 0x23a5 + 0x49dd;
                                    for (M = B[az(lw.P)](-0x1b * -0x149 + -0x2 * -0x3a9 + -0x1 * 0x2a05),
                                    P = 0x2 * 0xe93 + -0xf60 + -0xdc6; F[az(lw.Z)](P, 0x2 * -0x74f + -0x136b + 0x7 * 0x4df); P++)
                                        w = F[az(lw.j)](F[az(lw.c)](w, 0x112 * -0x13 + 0x12 * 0xfb + 0x2b1), F[az(lw.s)](0x5 * 0x7b + 0x1da3 + -0x2009, M)),
                                        F[az(lw.b)](k, F[az(lw.x)](H, 0x12b9 + 0xa * -0x226 + 0x2c4 * 0x1)) ? (k = -0x10 * -0x1c3 + -0x1446 + 0x1 * -0x7ea,
                                        T[az(lw.I)](F[az(lw.h)](W, w)),
                                        w = -0x17d6 + -0x92 * -0x1 + 0x1744) : k++,
                                        M >>= 0x2d * 0x59 + 0x1037 + 0x23 * -0xe9;
                                }
                                F[az(lw.v)](0x18b1 + -0x1 * -0xd7f + -0x2630, --Q) && (Q = Math[az(lw.J)](0x1 * 0x11ea + -0x59 * -0x2e + -0x21e6, I),
                                I++),
                                delete N[B];
                            } else {
                                for (M = L[B],
                                P = -0x1 * 0x2643 + -0x1566 + 0x3ba9; F[az(lw.e)](P, I); P++)
                                    w = F[az(lw.O)](F[az(lw.t)](w, 0x225a + -0x9d * -0x5 + -0x256a), F[az(lw.q)](0x1 * -0x211 + 0x18d7 + -0x16c5, M)),
                                    F[az(lw.z)](k, F[az(lw.F0)](H, -0x4ec + 0x1784 + -0x1297)) ? (k = 0x3d1 * 0xa + 0x68 * 0x2f + 0x7 * -0x82e,
                                    T[az(lw.I)](F[az(lw.F1)](W, w)),
                                    w = 0x2 * -0xe71 + -0x577 * -0x3 + -0x17 * -0x8b) : k++,
                                    M >>= -0x4 * 0x21e + 0x17 * -0xd1 + 0x1b4 * 0x10;
                            }
                            F[az(lw.z)](0x13c5 * -0x1 + -0x7 * 0x2 + 0x13d3, --Q) && (Q = Math[az(lw.Fd)](-0x250d + 0xd8b * -0x1 + -0x194d * -0x2, I),
                            I++),
                            L[V] = R++,
                            B = F[az(lw.Fz)](String, K);
                        }
                    if (F[az(lw.Y0)]('', B)) {
                        if (Object[az(lw.A)][az(lw.Y1) + az(lw.Y2)][az(lw.Y3)](N, B)) {
                            if (F[az(lw.Y4)](B[az(lw.P)](-0x2b1 * 0x2 + -0x490 + 0x9f2), 0xdc0 + 0x1 * 0x15e9 + -0x22a9 * 0x1)) {
                                for (P = 0x61 * -0x12 + 0x9e9 * 0x2 + -0xd00 * 0x1; F[az(lw.Y5)](P, I); P++)
                                    w <<= 0x19bb * -0x1 + -0xd0e + -0x7c2 * -0x5,
                                    F[az(lw.Y6)](k, F[az(lw.Y7)](H, 0xfe7 + 0x19f1 + -0x29d7)) ? (k = 0x63d + 0x480 + -0xabd,
                                    T[az(lw.Y8)](F[az(lw.Y9)](W, w)),
                                    w = 0x900 + 0xbd0 + 0x30 * -0x6f) : k++;
                                for (M = B[az(lw.P)](0x1535 + -0x13ed + -0x148),
                                P = -0x25d * -0x5 + -0x2fc * 0x1 + -0x8d5 * 0x1; F[az(lw.YF)](P, -0x1ca7 + -0x1cd0 + 0x1 * 0x397f); P++)
                                    w = F[az(lw.YY)](F[az(lw.YU)](w, -0x1424 + -0x2102 + -0x4d5 * -0xb), F[az(lw.Ya)](0x110f + -0x197c * -0x1 + -0x2a8a, M)),
                                    F[az(lw.YA)](k, F[az(lw.Yr)](H, 0x135b + 0x2 * 0xe6b + 0xc0c * -0x4)) ? (k = -0x11b7 + -0x1fbf + -0x3176 * -0x1,
                                    T[az(lw.L)](F[az(lw.Y9)](W, w)),
                                    w = -0x4 * -0x94d + -0x1c80 + -0x8b4) : k++,
                                    M >>= -0x1 * -0x22c7 + -0xf07 * -0x1 + 0x31cd * -0x1;
                            } else {
                                for (M = 0x18fc + 0x1016 + -0x2911,
                                P = -0xae3 + 0x7e * -0x36 + -0x1a1 * -0x17; F[az(lw.YD)](P, I); P++)
                                    w = F[az(lw.Yo)](F[az(lw.Yn)](w, -0x1a38 + 0xb * -0x31c + -0x1 * -0x3c6d), M),
                                    F[az(lw.Yi)](k, F[az(lw.Yy)](H, -0x1670 + 0x43 * 0x35 + -0x2 * -0x449)) ? (k = 0x199 * 0x15 + 0xc48 + -0x2dd5 * 0x1,
                                    T[az(lw.Y8)](F[az(lw.T)](W, w)),
                                    w = -0xe1 + -0x58d * -0x1 + -0x5c * 0xd) : k++,
                                    M = 0x2 * -0x1112 + -0x3b * 0x47 + -0x1 * -0x3281;
                                for (M = B[az(lw.YG)](0xb0e + 0x1 * 0x112f + 0x1 * -0x1c3d),
                                P = -0x665 + -0x209 + 0xa6 * 0xd; F[az(lw.YS)](P, 0x2 * -0x187 + 0x1853 + -0x1535); P++)
                                    w = F[az(lw.Ym)](F[az(lw.Yl)](w, 0x383 + 0x15f4 + -0x1976), F[az(lw.YE)](-0x2 * 0x2c7 + -0xb * 0x2a1 + 0x113d * 0x2, M)),
                                    F[az(lw.YH)](k, F[az(lw.u)](H, -0x1149 + 0x851 * 0x3 + -0x7a9)) ? (k = 0x1 * 0x18b3 + 0xa9c + -0x234f,
                                    T[az(lw.YW)](F[az(lw.YP)](W, w)),
                                    w = 0x1115 + 0x6 * 0xd4 + -0x160d) : k++,
                                    M >>= -0x187 * -0x16 + -0x1e79 + -0x64 * 0x8;
                            }
                            F[az(lw.YM)](-0x1891 + -0x1596 + 0x2e27, --Q) && (Q = Math[az(lw.Fd)](-0x189c + 0x4 * -0x26 + 0x1936, I),
                            I++),
                            delete N[B];
                        } else {
                            for (M = L[B],
                            P = 0xfcd * 0x1 + -0x1295 + 0x2c8; F[az(lw.YK)](P, I); P++)
                                w = F[az(lw.YV)](F[az(lw.YL)](w, -0x193a + 0x2a1 * 0x5 + 0xc16), F[az(lw.YN)](0x3 * 0x399 + 0x6 * -0x1a3 + -0xf8 * 0x1, M)),
                                F[az(lw.Yg)](k, F[az(lw.YB)](H, -0x59 * -0x3a + -0x1 * -0x159 + -0x2 * 0xac1)) ? (k = -0x393 + -0x67 * 0x45 + 0x1f56,
                                T[az(lw.YQ)](F[az(lw.YR)](W, w)),
                                w = -0x329 + -0xe78 * 0x2 + -0x3 * -0xab3) : k++,
                                M >>= 0x219d * -0x1 + -0x177 * 0x2 + 0x1 * 0x248c;
                        }
                        F[az(lw.Yf)](0x7b9 + -0x21b3 + 0x5 * 0x532, --Q) && (Q = Math[az(lw.J)](0x2 * 0x8bd + -0x577 * 0x1 + -0xc01, I),
                        I++);
                    }
                    for (M = 0x1 * 0x2465 + 0xc * 0x30b + -0x48e7,
                    P = -0x916 + 0x203 + 0x713; F[az(lw.M)](P, I); P++)
                        w = F[az(lw.Yu)](F[az(lw.YI)](w, -0x23d4 + 0x13 * -0x207 + -0x266 * -0x1f), F[az(lw.YE)](-0x1928 + -0x1e19 + 0x3742 * 0x1, M)),
                        F[az(lw.YT)](k, F[az(lw.u)](H, 0x283 * -0xd + 0x207e + 0x15 * 0x2)) ? (k = -0xabe + 0x1 * 0x19c + 0x1 * 0x922,
                        T[az(lw.Yw)](F[az(lw.Yk)](W, w)),
                        w = -0x1d75 * 0x1 + 0x1bd7 * -0x1 + 0x394c) : k++,
                        M >>= 0x1 * -0x67f + 0xca0 + -0x620;
                    for (; ; ) {
                        if (w <<= 0x662 + 0x2166 + -0x11 * 0x257,
                        F[az(lw.Yp)](k, F[az(lw.Yv)](H, 0x26c1 + 0x1652 + -0x3d12))) {
                            T[az(lw.YX)](F[az(lw.YC)](W, w));
                            break;
                        }
                        k++;
                    }
                    return T[az(lw.YZ)]('');
                }

let L = {
    FW: "https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm",
    hash: "",
    host: "mxsa.mxbc.net",
    hostname: "mxsa.mxbc.net",
    pathname: "/api/v1/h5/marketing/secretword/confirm",
    port: "",
    protocol: "https:",
    search: ""
},
    N = '{"marketingId":"1816854086004391938","round":"11:00","secretword":"147","sign":"730195d69c0fa2a55fec93a97f3e1645","s":2,"stamp":1722396472208}';

function get_sig(url){
        let z = sig(url)
        return ua(z, true)
}
var a = get_sig(L["FW"] + L["hash"] + N)
console.log(a);
//
// de(L,N)