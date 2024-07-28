import random


INTRO = 'What number is missing in the progression?'


def generate_progression() -> list:
    """
    Generates and returns a random arithmetic progression "progression_list"
    as a list of strings.

    To generate a progression we need:
        - initial number -> "progression_num" : randomly generated integer
        - progression step -> "progression_step" : randomly generated integer
        - progression length -> "progression_length" : randomly generated
        integer

    Knowing the above parameters, we generate a progression using
    the "for" loop.

    Args:
        - the required variables are generated in the function.

    Returns:
        Arithmetic progression as a list of strings.
        For example:

        generate_progression() =>
        => [901, 905, 909, 913, 917, 921, 925, 929, 933, 937]
    """
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
    Generates a random arithmetic progression "progression_list"
    as a list of strings in generate_progression().
    Randomly selects the "progression_list" element by "index" and replaces
    it with "..". The replaced progression element -> "answer".
    Returns a string "question" with modified "progression_list" and
    a string "answer".

    Args:
        - the required variables are generated in the function.

    Returns:
        A tuple consisting of a string "question" with modified
        "progression_list" and a string "answer".
        For example:

        game_logic() => ('901 905 909 913 .. 921 925 929 933 937', '917')
    """
    progression_list = generate_progression()
    index = random.randint(0, (len(progression_list) - 1))
    answer = progression_list[index]
    progression_list[index] = '..'
    question = ' '.join(progression_list)
    return (question, answer)
