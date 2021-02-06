from random import randint

from brain_games import core


def prepare_round():
    random_number = randint(1, 100)
    question_text = str(random_number)
    right_answer = 'yes' if random_number % 2 == 0 else 'no'
    return question_text, right_answer


def main():
    game_description = \
        'Answer "yes" if the number is even, otherwise answer "no".'

    core.run_game(game_description, prepare_round)
