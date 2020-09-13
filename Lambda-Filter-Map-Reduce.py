import os

os.rename('Lambda.py', 'Lambda-Filter-Map-Reduce.py')


def bqf(a):
    return lambda x: a * x ** 2 + a * x + a


def biqf(a, b, c, d):
    return lambda x: a * x ** 3 + b * x ** 2 + c * x + d


values = [51, 54, 54, 54, 1, 5161, 651, 35, 1, 11, 5, 65, 65, 62, 3]
m = map(lambda x: 1 * x ** 3 + 2 * x ** 2 + 3 * x + 4, values)

print(list(filter(lambda x: x > 10, m)))

# reduce function is used for multipying inside a list. \'for\' loop can be used
