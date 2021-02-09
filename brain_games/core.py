import prompt

GAME_ROUNDS_COUNT = 3


def run_game(game_description, prepare_round):
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(f'{game_description}')

    round_number = 1

    while round_number <= GAME_ROUNDS_COUNT:
        round_number += 1
        question_text, right_answer = prepare_round()

        print(f'Question: {question_text}')

        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'."
                  f"\nLet's try again, {user_name}!")
            return None

    print(f'Congratulations, {user_name}!')
