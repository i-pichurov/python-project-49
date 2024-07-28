import random


INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    """Checks if an integer from the argument "num" is even
    and returns boolean result.

    Args:
        num: integer that is checked for evenness.

    Returns:
        True - if the remainder of dividing "num" by 2 == 0.
        False - if the remainder of dividing "num" by 2 != 0.
        For example:

        is_even(4) => True
        is_even(3) => False
    """
    if num % 2 == 0:
        return True
    else:
        return False


def game_logic() -> tuple:
    """
    Randomly generates an integer: "random_number", checks it for evenness.
    Returns a string "question" with the value of "random_number" that is
    checked for evenness and the result of the check in
    is_even(random_number: int) as a string "answer"
    with value: 'yes' or 'no'.

    Args:
        - the required variables are generated in the function.

    Returns:
        A tuple consisting of a string "question" with the value of
        "random_number" and the result of the check
        as a string "answer" with value: 'yes' or 'no'.
        For example:

        game_logic() => ('6', 'yes')
        game_logic() => ('87', 'no')
    """
    random_number = random.randint(1, 100)
    question = f'{random_number}'
    if is_even(random_number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
