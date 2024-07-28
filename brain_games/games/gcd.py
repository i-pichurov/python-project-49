import random


INTRO = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(num1: int, num2: int) -> int:
    """
    Takes two integers as arguments: "num1" and "num2" -
    and returns their greatest common divisor in integer "divisor".

    Args:
        num1: defines the value of the first integer.
        num1: defines the value of the second integer.

    Returns:
        Integer "divisor" - the greatest common divisor of "num1" and "num2".
        For example:

        calculate_gcd(899, 2761) => 1
        calculate_gcd(450, 150) => 150
    """
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


def game_logic():
    """
    Randomly generates two integers: "num1" and "num2".
    Returns a string "question" with the values of "num1" and "num2"
    whose greatest common divisor needs to be calculated,
    and the integer result of the calculation in
    calculate_gcd(num1: int, num2: int).

    Args:
        - the required variables are generated in the function.

    Returns:
        A tuple consisting of a string "question" with the values
        of "num1" and "num2",
        and the integer result of the calculation in
        calculate_gcd(num1: int, num2: int).
        For example:

        game_logic() => ('899 2761', 1)
        game_logic() => ('450 150', 150)
    """
    num1 = random.randint(1, 10000)
    num2 = random.randint(1, 10000)
    question = f'{num1} {num2}'
    return (question, calculate_gcd(num1, num2))
