all: sort-imports format type-check test

.PHONY: sort-imports format type-check test

SHELL=/bin/bash
SHELLFLAGS=-euo pipefail -c

sort-imports:
	python3 -m isort --atomic app tests

format:
	python3 -m black app tests

type-check:
	python3 -m mypy app

test:
	python3 -m pytest -o log_cli=true tests
