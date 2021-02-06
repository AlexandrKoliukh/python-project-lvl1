"""CLI functions."""

import prompt


def welcome_user():
    """Prompt user name and greeting."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}'.format(name=name))  # noqa: WPS421
