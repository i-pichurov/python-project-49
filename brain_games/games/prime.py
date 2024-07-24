import random


INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """Checks if a number is prime."""
    if num > 1:
        for i in range(2, (num + 1)):
            if (num % i == 0) and (i != num):
                return False
        return True
    else:
        return False


def game_logic():
    """
    Generates a random number.
    Returns question and answer.
    """
    num = random.randint(1, 3571)
    question = f'{num}'
    if is_prime(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
