from random import randint

DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10


def calculate_step_value(init, step, current):
    return init + step * current


def prepare_round():
    init_number = randint(1, 50)
    step_value = randint(1, 25)
    hidden_element_index = randint(0, PROGRESSION_LENGTH - 1)

    right_answer = str(
        calculate_step_value(init_number, step_value, hidden_element_index))

    question = ''
    current_step = 0

    while current_step < PROGRESSION_LENGTH:
        if hidden_element_index == current_step:
            question += '..'
        else:
            question += str(
                calculate_step_value(init_number, step_value, current_step))
        if current_step != PROGRESSION_LENGTH - 1:
            question += ' '
        current_step += 1

    return question, right_answer
