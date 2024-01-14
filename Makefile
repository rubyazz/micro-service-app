.PHONY: psql up down venv check-deps update-deps install-deps isort black mypy flake8 bandit lint test migrate serve

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

VENV=.venv
PYTHON=$(VENV)/bin/python3

cmd-exists-%:
	@hash $(*) > /dev/null 2>&1 || \
		(echo "ERROR: '$(*)' must be installed and available on your PATH."; exit 1)

psql: cmd-exists-psql
	psql "${DATABASE_URL}"

up:  ## Run Docker Compose services
	docker-compose -f docker-compose.local.yml up -d

down:  ## Shutdown Docker Compose services
	docker-compose -f docker-compose.local.yml down

venv: requirements-dev.txt Makefile
	python3 -m pip install --upgrade pip setuptools wheel
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements-dev.txt

check-deps:  ## Check new versions and update deps
	$(PYTHON) -m pur -r requirements-dev.txt -d

update-deps:  ## Check new versions and update deps
	$(PYTHON) -m pur -r requirements-dev.txt

install-deps:  ## Install dependencies
	$(PYTHON) -m pip install -r requirements-dev.txt

isort:
	$(PYTHON) -m isort --check-only .

black:
	$(PYTHON) -m black --check .

mypy:
	$(PYTHON) -m mypy .

flake8:
	$(PYTHON) -m flake8 .

bandit:
	$(PYTHON) -m bandit -r app

lint: isort black mypy flake8 bandit

test:  ## Run tests
	$(PYTHON) -m pytest

migrate:  ## Apply latest alembic migrations
	$(PYTHON) -m alembic upgrade head

run:
	uvicorn main:app --reload --port=8000

linter:
	pre-commit run --all-files
