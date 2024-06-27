#!/usr/bin/env python3
import random


def br_gcd():
    intro = 'Find the greatest common divisor of given numbers.'
    num1 = random.randint(1, 10000)
    num2 = random.randint(1, 10000)
    question = f'{num1} {num2}'

    if num1 > num2:
        dividend = num1
        divider = num2
    else:
        dividend = num2
        divider = num1
    i = dividend % divider
    while i > 0:
        dividend = divider
        divider = i
        i = dividend % divider
    return (intro, question, divider)
