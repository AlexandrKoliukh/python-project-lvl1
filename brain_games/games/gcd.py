from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def prepare_round():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)

    question = f'{number_1} {number_2}'
    right_answer = str(gcd(number_1, number_2))
    return question, right_answer
