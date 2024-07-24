import random


INTRO = 'What is the result of the expression?'


def is_even(random_number):
    if random_number % 2 == 0:
        return True
    else:
        return False


def game_logic():
    random_number = random.randint(1, 100)
    question = f'{random_number}'
    if is_even(random_number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
