import brain_games.games.welcome
import prompt


def start_game(game):
    name = brain_games.games.welcome.welcome_user()
    print(game()[0])
    i = 0
    while i < 3:
        question, answer = game()[1:3]
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
