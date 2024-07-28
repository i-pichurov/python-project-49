import prompt


def welcome_user():
    """
    Greets the user by the name they entered.
    Returns the username in the string "name".

    Args:
        - the required variables are generated in the function.

    Returns:
        The username in the string "name".
        For example:

        welcome_user() =>
        => 'Welcome to the Brain Games!'
        'May I have your name? ' -> entered: 'Mike'
        'Hello, Mike'
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def start_game(module):
    """
    Greets the user by the name in welcome_user()
    Takes a mini-game module as an argument.

    Depending on the module in the argument, asks the user question from
    "question = module.game_logic()[0]".

    Compares the "user_answer" entered by user with
    the "answer = module.game_logic()[1]".
    If answered correctly, confirms it and generates a new question.
    If the answer is incorrect, rejects it and breaks the function.
    After 3 correct answers in a row, congratulates the user and
    completes the function.

    Args:
        module : one of the modules with a mini-game from the directory:
        brain_games/games

    Returns:
        - only displays messages about the game progress.
        For example:

        start_game(brain_games.games.even) =>
        => 'Welcome to the Brain Games!'
        'May I have your name? ' -> entered: 'John'
        'Hello, John'
        'Answer "yes" if the number is even, otherwise answer "no".'
        'Question: 73'
        'Your answer: ' -> entered: 'no'
        'Correct!'
        'Question: 71'
        'Your answer: ' -> entered 'yes'
        "'yes' is wrong answer ;(. Correct answer was 'no'."
        'Let's try again, John!'
    """
    name = welcome_user()
    print(module.INTRO)
    i = 0
    while i < 3:
        question, answer = module.game_logic()[0:2]
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if str(answer) == user_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{user_answer}' is wrong answer "
                  f";(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')
