from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def prepare_round():
    number = randint(1, 100)
    question = str(number)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return question, right_answer
