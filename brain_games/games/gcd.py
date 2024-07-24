import random


INTRO = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(num1, num2):
    """Returns GCD."""
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
    Randomly generates number1 and number2.
    Returns question and answer.
    """
    num1 = random.randint(1, 10000)
    num2 = random.randint(1, 10000)
    question = f'{num1} {num2}'
    return (question, calculate_gcd(num1, num2))
