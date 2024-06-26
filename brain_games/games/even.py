#!/usr/bin/env python3
import prompt
import random
import brain_games.games.welcome


def even_check(random_number):
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even_game():
    name = brain_games.games.welcome.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if even_check(random_number) == answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{even_check(random_number)}'.\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')
