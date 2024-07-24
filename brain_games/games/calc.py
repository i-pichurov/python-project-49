import random


def calculation(num1, num2, operator):
    if operator == "-":
        result = num1 - num2
    elif operator == "+":
        result = num1 + num2
    else:
        result = num1 * num2
    return result


def game_logic():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operators_list = ["-", "+", "*"]
    operator = random.choice(operators_list)
    question = f'{num1} {operator} {num2}'
    return (question, str(calculation(num1, num2, operator)))


intro = 'What is the result of the expression?'
