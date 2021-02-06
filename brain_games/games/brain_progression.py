from random import randint

from brain_games import core


PROGRESSION_LENGTH = 10


def prepare_round():
    progression_step = randint(1, 25)
    hidden_element_index = randint(0, PROGRESSION_LENGTH - 1)

    progression_string = ''
    current = randint(1, 50)
    index = 0
    right_answer = ''

    while index < PROGRESSION_LENGTH:
        if hidden_element_index == index:
            progression_string += '..'
            right_answer = str(current)
        else:
            progression_string += str(current)
        if index != PROGRESSION_LENGTH - 1:
            progression_string += ' '
        current += progression_step
        index += 1

    question_text = progression_string
    return question_text, right_answer


def main():
    game_description = \
        'What number is missing in the progression?'

    core.run_game(game_description, prepare_round)
