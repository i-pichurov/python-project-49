#!/usr/bin/env python3
import random


def br_calc():
    intro = 'What is the result of the expression?'
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = ["-", "+", "*"]
    op = random.choice(operator)
    question = f'{num1}{op}{num2}'
    if op == "-":
        answer = num1 - num2
        return (intro, question, answer)
    elif op == "+":
        answer = num1 + num2
        return (intro, question, answer)
    else:
        answer = num1 * num2
        return (intro, question, answer)
