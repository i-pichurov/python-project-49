import random


INTRO = 'What number is missing in the progression?'


def generate_progression():
    """Generates and returns a random arithmetic progression"""
    progression_num = random.randint(1, 1000)
    progression_length = random.randint(5, 10)
    progression_step = random.randint(1, 10)
    progression_list = []

    for i in range(progression_length):
        progression_list.append(str(progression_num))
        progression_num += progression_step
    return progression_list


def game_logic():
    """
    Replaces any number in a random arithmetic progression with ".." .
    Returns question and answer.
    """
    progression_list = generate_progression()
    index = random.randint(0, (len(progression_list) - 1))
    answer = progression_list[index]
    progression_list[index] = '..'
    question = ' '.join(progression_list)
    return (question, answer)
