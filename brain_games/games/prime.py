from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
    number = randint(1, 100)

    question = str(number)
    right_answer = 'yes' if is_prime(number) else 'no'
    return question, right_answer
