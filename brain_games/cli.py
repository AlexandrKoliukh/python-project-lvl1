"""CLI functions."""
# flake8: noqa: WPS421

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
