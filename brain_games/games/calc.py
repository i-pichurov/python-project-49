import random


INTRO = 'What is the result of the expression?'


def calculate_result(num1, num2, operator):
    """
    Checks the operator and 
    returns the result of an operation between number1 and number2.
    """
    if operator == "-":
        result = num1 - num2
    elif operator == "+":
        result = num1 + num2
    else:
        result = num1 * num2
    return result


def game_logic():
    """
    Randomly generates number1 and number2.
    Randomly selects the operator.
    Returns question and answer.
    """
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operators_list = ["-", "+", "*"]
    operator = random.choice(operators_list)
    question = f'{num1} {operator} {num2}'
    return (question, calculate_result(num1, num2, operator))
