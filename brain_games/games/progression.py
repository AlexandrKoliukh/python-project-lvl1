from random import randint

from brain_games import core

PROGRESSION_LENGTH = 10


def calculate_step_value(init, step, current):
    return init + step * current


def prepare_round():
    init_number = randint(1, 50)
    step_value = randint(1, 25)
    hidden_element_index = randint(0, PROGRESSION_LENGTH - 1)

    right_answer = str(
        calculate_step_value(init_number, step_value, hidden_element_index))

    question_text = ''
    current_step = 0

    while current_step < PROGRESSION_LENGTH:
        if hidden_element_index == current_step:
            question_text += '..'
        else:
            question_text += str(
                calculate_step_value(init_number, step_value, current_step))
        if current_step != PROGRESSION_LENGTH - 1:
            question_text += ' '
        current_step += 1

    return question_text, right_answer


def main():
    game_description = \
        'What number is missing in the progression?'

    core.run_game(game_description, prepare_round)
