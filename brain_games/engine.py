import prompt


def welcome_user():
    """
    Greets the user and
    returns the name he specified.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def start_game(module):
    """
    Greets the user
    Depending on the module in the argument, asks the user questions
    Compares the user's answer with the "answer" variable
    If answered correctly, generates a new question
    If the answer is incorrect, the function is aborted
    After 3 correct answers in a row, congratulates the user
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
