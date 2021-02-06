from random import randint
from random import choice

from brain_games import core


AVAILABLE_OPERATIONS = ('+', '-', '*')


def prepare_round():
    operation = choice(AVAILABLE_OPERATIONS)
    operator1 = randint(1, 100)
    operator2 = randint(1, 100)
    question_text = f'{operator1} {operation} {operator2}'
    right_answer = str(eval(question_text))
    return question_text, right_answer


def main():
    game_description = \
        'What is the result of the expression?'

    core.run_game(game_description, prepare_round)
