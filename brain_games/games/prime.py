import random


def br_prime():
    intro = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    num = random.randint(1, 3571)
    question = f'Question: {num}'
    if num > 1:
        answer = 'yes'
        for i in range(2, (num + 1)):
            if (num % i == 0) and (i != num):
                answer = 'no'
                break
    else:
        answer = 'no'
    return (intro, question, str(answer))
