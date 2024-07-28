import random


INTRO = 'What is the result of the expression?'


def calculate_result(num1: int, num2: int, operator: str) -> int:
    """
    Performs the arithmetic operation from the argument "operator"
    between the integers from "num1" and "num2".

    Args:
        num1: defines the value of the first integer.
        num1: defines the value of the second integer.
        operator: defines the value of the arithmetic
          operation applied to num1 and num2.

    Returns:
        Integer - result of the arithmetic operation from the
        argument "operator" between the numbers from "num1" and "num2".
        If the operation is not supported, print 'Incorrect operator.'
        For example:

        calculate_result(1, 4, "+") => 5
        calculate_result(1, 4, "/") => "Incorrect operator."
    """

    if operator == "-":
        return num1 - num2
    elif operator == "+":
        return num1 + num2
    elif operator == "*":
        return num1 * num2
    else:
        print("Incorrect operator.")


def game_logic() -> tuple:
    """
    Randomly generates two integers: "num1" and "num2".
    Randomly generates an arithmetic operator": "operators_list" -> "operator".
    Returns a string "question" with the generated operation and numbers,
    as well as the result of this operation as an integer.

    Args:
        - the required variables are generated in the function.

    Returns:
        A tuple consisting of a string with the generated
        arithmetic operation and the result of that operation as an integer.
        For example:

        game_logic() => ('27 - 86', -59)
        game_logic() => ('35 * 31', 1085)
    """
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operators_list = ["-", "+", "*"]
    operator = random.choice(operators_list)
    question = f'{num1} {operator} {num2}'
    return (question, calculate_result(num1, num2, operator))
