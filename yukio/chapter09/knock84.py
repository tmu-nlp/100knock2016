from knock83 import measure_frequency
from collections import defaultdict
import math

def make_matrix():
    f_t_c, f_t, f_c, N = measure_frequency()
    X_t_c = defaultdict(lambda: 0)

    for key, value in sorted(f_t_c.items()):
        if value >= 10:
            token, context = key.split(" ")
            if math.log(N * value / (f_t[token] * f_c[context]), 2) > 0:
                X_t_c[key] = math.log(N * value / (f_t[token] * f_c[context]), 2)

    return X_t_c

if __name__ == "__main__":
    X_t_c = make_matrix()
    for key, value in sorted(X_t_c.items()):
        print("X({}) : {}".format(key.replace(" ", ", "), value))
