from random import randint

from brain_games import core


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def prepare_round():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)

    question_text = f'{number_1} {number_2}'
    right_answer = str(gcd(number_1, number_2))
    return question_text, right_answer


def main():
    game_description = \
        'Find the greatest common divisor of given numbers.'

    core.run_game(game_description, prepare_round)
