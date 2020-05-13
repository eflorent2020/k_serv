#!/bin/sh
flake8 .
python3 -m pytest -m coverage
coverage report | grep -v /usr
bandit .