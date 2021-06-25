import math


def num_BTC(b):

    c = float(0)

    half_time = b // 210000
    print(half_time)
    remain = b % 210000
    i = 0
    while i < half_time:
        c += 50 * 210000 * pow(0.5, i)
        i += 1

    c += remain * pow(0.5, i) * 50
    # print(i)
    # print(c)

    return c


# num_BTC(10)