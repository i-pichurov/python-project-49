#!/usr/bin/env python3
import random


def br_calc():
    intro = 'What is the result of the expression?'
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operators_list = ["-", "+", "*"]
    operator = random.choice(operators_list)
    question = f'Question: {num1} {operator} {num2}'
    if operator == "-":
        answer = num1 - num2
    elif operator == "+":
        answer = num1 + num2
    else:
        answer = num1 * num2
    return (intro, question, str(answer))
