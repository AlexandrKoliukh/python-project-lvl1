.DEFAULT_GOAL := republish

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

republish:
	rm -rf dist
	make build
	make publish

lint:
	poetry run flake8 brain_games

