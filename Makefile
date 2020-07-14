all: sort-imports format type-check test

.PHONY: sort-imports format type-check test build run

SHELL=/bin/bash
SHELLFLAGS=-euo pipefail -c

sort-imports:
	python3 -m isort --atomic app.py test_app.py

format:
	python3 -m black app.py test_app.py

type-check:
	python3 -m mypy app.py

test:
	python3 -m pytest -o log_cli=true test_app.py

build: all
	docker build --tag emoji-app:latest .

run:
	docker run --rm --name emoji-app -p 3001:3001/udp emoji-app:latest