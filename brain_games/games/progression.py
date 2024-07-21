#!/usr/bin/env python3
import random


def progression():
    progression_num = random.randint(1, 1000)
    progression_length = random.randint(5, 10)
    progression_step = random.randint(1, 10)
    progression_list = []

    for i in range(progression_length):
        progression_list.append(str(progression_num))
        progression_num += progression_step
    return progression_list


def progression_num_swap(progression_list):
    index = random.randint(0, (len(progression_list) - 1))
    answer = progression_list[index]
    progression_list[index] = '..'
    progression_list = ' '.join(progression_list)
    return (answer, progression_list)


def br_progression():
    intro = 'What number is missing in the progression?'
    answer, question = progression_num_swap(progression())[0:2]
    return (intro, question, answer)
