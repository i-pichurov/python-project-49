import random


INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    """Checks if a number is even."""
    if random_number % 2 == 0:
        return True
    else:
        return False


def game_logic():
    """
    Generates a random number.
    Returns question and answer.
    """
    random_number = random.randint(1, 100)
    question = f'{random_number}'
    if is_even(random_number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
