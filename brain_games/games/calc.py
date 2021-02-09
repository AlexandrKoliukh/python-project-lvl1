from random import randint, choice

from brain_games import core

AVAILABLE_OPERATIONS = ('+', '-', '*')


def prepare_round():
    operation = choice(AVAILABLE_OPERATIONS)
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question_text = f'{number_1} {operation} {number_2}'
    right_answer = str(eval(question_text))
    return question_text, right_answer


def main():
    game_description = \
        'What is the result of the expression?'

    core.run_game(game_description, prepare_round)
