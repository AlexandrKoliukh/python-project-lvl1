from random import randint

from brain_games import core


def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i < n / 2:
        if n % i == 0:
            return False
        i += 1

    return True


def prepare_round():
    random_number = randint(1, 100)

    question_text = str(random_number)
    right_answer = 'yes' if is_prime(random_number) else 'no'
    return question_text, right_answer


def main():
    game_description = \
        'Answer "yes" if given number is prime. Otherwise answer "no".'

    core.run_game(game_description, prepare_round)
