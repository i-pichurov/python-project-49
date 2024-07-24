import random


def generate_progression():
    progression_num = random.randint(1, 1000)
    progression_length = random.randint(5, 10)
    progression_step = random.randint(1, 10)
    progression_list = []

    for i in range(progression_length):
        progression_list.append(str(progression_num))
        progression_num += progression_step
    return progression_list


def game_logic():
    progression_list = generate_progression()
    index = random.randint(0, (len(progression_list) - 1))
    answer = progression_list[index]
    progression_list[index] = '..'
    question = ' '.join(progression_list)
    return (question, answer)


intro = 'What number is missing in the progression?'
