#Brain Games

[![Actions Status](https://github.com/AlexandrKoliukh/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/AlexandrKoliukh/python-project-lvl1/actions)
![Python CI](https://github.com/AlexandrKoliukh/python-project-lvl1/workflows/Python%20CI/badge.svg?branch=main)
[![Maintainability](https://api.codeclimate.com/v1/badges/e4eefaadb350802026a0/maintainability)](https://codeclimate.com/github/AlexandrKoliukh/python-project-lvl1/maintainability)

The package contains five simple mathematics quiz games:

- Even check `brain-even`
- Calculator `brain-calc`
- The greatest common divider `brain-gcd`
- Arithmetic progression `brain-progression`
- Prime number `brain-prime`

## Setup

See `Makefile` for help

    make install

## Local publish

    make build
	make publish
    make package-install

## Using

    brain-<game-name> [even, calc, gcd, progression, prime]
