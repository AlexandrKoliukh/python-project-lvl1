#! usr/bin/env python3
"""Package index."""

from brain_games import cli


def main():
    """Brain games main."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    cli.welcome_user()


if __name__ == '__main__':
    main()
