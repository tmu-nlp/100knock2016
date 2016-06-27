from collections import defaultdict

def measure_frequency():
    f_t_c = defaultdict(lambda: 0)
    f_t = defaultdict(lambda: 0)
    f_c = defaultdict(lambda: 0)
    N = 0

    for line in open("token_context_82.txt", "r"):
        token, context = line.strip("\n").split("\t")
        f_t_c["{} {}".format(token, context)] += 1
        f_t[token] += 1
        f_c[context] += 1
        N += 1

    return f_t_c, f_t, f_c, N

if __name__ == "__main__":
    f_t_c, f_t, f_c, N = measure_frequency()
    for key, value in sorted(f_t_c.items()):
        print("f({}) : {}".format(key.replace(" ", ", "), value))
    for key, value in sorted(f_t.items()):
        print("f({}, *) : {}".format(key, value))
    for key, value in sorted(f_c.items()):
        print("f(*, {}) : {}".format(key, value))
    print("N : {}".format(N))
