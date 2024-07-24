import random


def is_prime(num):
    if num > 1:
        for i in range(2, (num + 1)):
            if (num % i == 0) and (i != num):
                return False
        return True
    else:
        return False


def game_logic():
    num = random.randint(1, 3571)
    question = f'{num}'
    if is_prime(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)


intro = 'Answer "yes" if given number is prime. Otherwise answer "no".'
