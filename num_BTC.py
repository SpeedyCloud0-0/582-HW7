import math


def num_BTC(b):

    c = float(0)
    half_time = b / 210000
    remain = b % 210000
    i = 0
    while i < half_time:
        c += 50 * 210000 * pow(0.5, i)

    c += remain * pow(0.5, i) * 50

    return c


