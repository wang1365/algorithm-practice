TAYLOR_N = 10


# TAYLOR FORMULA
# f(x) = f(x0) +
#       + 1/2! * f'(x0)   * (x-x0)
#       + 1/2! * f''(x0)  * (x-x0)**2
#       + 1/3! * f'''(x0) * (x-x0)**3
#       ...
#       + 1/n! * fn(x0)   * (x-x0)**n

def power_of_e(x):
    def f(x, n):
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial * i
        return float(x ** n) / factorial

    # return sum(f(x, i) for i in range(0, TAYLOR_N + 1))
    return sum(f(x, i) for i in range(0, 100 + 1))

    # return 1 + x + x ** 2 / 2 + x ** 3 / (2 * 3) + x ** 4 / (2 * 3 * 4) + x ** 5 / (2 * 3 ** 4 * 5)


# This function works if x is nearby 0 because we use sin(0) as the basic point
def sin(x):
    def f(x, n):
        if n % 2 == 0:
            return 0
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial * i

        sign = -1 if ((n - 1) / 2) % 2 == 1 else 1
        return sign * float(x ** n) / factorial

    return sum(f(x, i) for i in range(0, TAYLOR_N + 1))


if __name__ == '__main__':
    import math

    print math.e, power_of_e(1)
    print math.e ** 2, power_of_e(2)
    print math.e ** 3, power_of_e(3)
    print math.e ** 1.89, power_of_e(1.89)

    print 'sin(0):', math.sin(0), sin(0)
    print 'sin(0.5):', math.sin(0.5), sin(0.5)
    print 'sin(pi/2):', math.sin(math.pi/2), sin(math.pi/2)
    print 'sin(2):', math.sin(2), sin(2)
    print 'sin(3):', math.sin(3), sin(3)
    print 'sin(pi):', math.sin(math.pi), sin(math.pi)
    print 'sin(4):', math.sin(4), sin(4)
    print 'sin(5):', math.sin(5), sin(5)
