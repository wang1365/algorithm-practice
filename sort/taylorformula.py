TAYLOR_N = 10


# TAYLOR FORMULA
# f(x) = f(x0) +
#       + f'(x0) * (x-x0)
#       + 1/2 * f''(x0) * (x-x0)**2
#       + 1/2*3 * f'''(x0) * (x-x0)**3
#       + 1/n! * fn(x0) * (x-x0)**n

def power_of_e(x):
    def f(x, n):
        factorial = 1
        for i in range(1, int(n) + 1):
            factorial = factorial * i
        return float(x ** int(n)) / factorial

    ret = 1
    for i in range(1, TAYLOR_N + 1):
        ret += f(x, i)

    return ret
    # return 1 + x + x ** 2 / 2 + x ** 3 / (2 * 3) + x ** 4 / (2 * 3 * 4) + x ** 5 / (2 * 3 ** 4 * 5)


if __name__ == '__main__':
    import math

    print math.e, power_of_e(1)
    print math.e ** 2, power_of_e(2)
    print math.e ** 3, power_of_e(3)
