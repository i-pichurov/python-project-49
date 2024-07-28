import random


INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    """Checks if an integer from the argument "num" is prime
    and returns boolean result.

    Args:
        num: integer for check.

    Returns:
        True - if "num" is divisible without remainder only by itself.
        False - if "num" is divisible without remainder by other numbers.
        For example:

        is_prime(17) => True
        is_prime(4) => False
    """
    if num > 1:
        for i in range(2, (num + 1)):
            if (num % i == 0) and (i != num):
                return False
        return True
    else:
        return False


def game_logic():
    """
    Randomly generates an integer: "random_number", checks if it is prime.
    Returns a string "question" with the value of "random_number" that is
    checked and the result of the check in
    is_prime(random_number: int) as a string "answer"
    with value: 'yes' or 'no'.

    Args:
        - the required variables are generated in the function.

    Returns:
        A tuple consisting of a string "question" with the value of
        "random_number" and the result of the check
        as a string "answer" with value: 'yes' or 'no'.
        For example:

        game_logic() => ('17', 'yes')
        game_logic() => ('4', 'no')
    """
    num = random.randint(1, 3571)
    question = f'{num}'
    if is_prime(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
