import random


def gcd_calc(num1, num2):
    if num1 > num2:
        dividend = num1
        divisor = num2
    else:
        dividend = num2
        divisor = num1
    i = dividend % divisor
    while i > 0:
        dividend = divisor
        divisor = i
        i = dividend % divisor
    return divisor


def func():
    num1 = random.randint(1, 10000)
    num2 = random.randint(1, 10000)
    question = f'{num1} {num2}'
    return (question, str(gcd_calc(num1, num2)))


intro = 'Find the greatest common divisor of given numbers.'
