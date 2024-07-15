#!/usr/bin/env python3
import random


def br_progression():
    intro = 'What number is missing in the progression?'
    progression_num = random.randint(1, 1000)
    progression_length = random.randint(5, 10)
    progression_step = random.randint(1, 10)
    progression_list = []
    question = ''

    for i in range(progression_length):
        progression_list.append(progression_num)
        progression_num += progression_step

    answer = progression_list[random.randint(0, (progression_length - 1))]

    for i in range(progression_length):
        if progression_list[i] == answer:
            question = f'{question} ..'
        else:
            question = f'{question} {progression_list[i]}'

    return (intro, question, str(answer))
