from random import randint, choice
import operator

DESCRIPTION = 'What is the result of the expression?'

AVAILABLE_OPERATIONS = ('+', '-', '*')


def calculate(sign, number_1, number_2):
    if sign == '-':
        operation = operator.sub
    elif sign == '+':
        operation = operator.add
    elif sign == '*':
        operation = operator.mul
    return operation(number_1, number_2)


def prepare_round():
    operation = choice(AVAILABLE_OPERATIONS)
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = f'{number_1} {operation} {number_2}'
    right_answer = str(calculate(operation, number_1, number_2))
    return question, right_answer
