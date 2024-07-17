#!/usr/bin/env python3
import random


def br_gcd():
    intro = 'Find the greatest common divisor of given numbers.'
    num1 = random.randint(1, 10000)
    num2 = random.randint(1, 10000)
    question = f'Question: {num1} {num2}'

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
    return (intro, question, str(divisor))
