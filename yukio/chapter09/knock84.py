from knock83 import measure_frequency
from collections import defaultdict
import math

def make_matrix():
    f_t_c, f_t, f_c, N = measure_frequency()
    X_t_c = defaultdict(lambda: defaultdict(lambda: 0))

    for key, value in sorted(f_t_c.items()):
        if value >= 20:
            token, context = key.split(" ")
            if math.log(N * value / (f_t[token] * f_c[context]), 2) > 0:
                X_t_c[token][context] = math.log(N * value / (f_t[token] * f_c[context]), 2)

    return X_t_c

if __name__ == "__main__":
    X_t_c = make_matrix()
    for token, dic in sorted(X_t_c.items()):
        for context, value in sorted(dic.items()):
            print("X({}, {}) : {}".format(token, context, value))
