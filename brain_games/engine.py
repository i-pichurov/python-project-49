import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def start_game(module):
    name = welcome_user()
    print(module.intro)
    i = 0
    while i < 3:
        question, answer = module.game_logic()[0:2]
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{user_answer}' is wrong answer "
                  f";(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')
