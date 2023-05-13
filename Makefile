lint:
	poetry run flake8 gendiff

install:
	poetry install

gendiff:
	poetry run gendiff

test:
	poetry run pytest

test-coverage:
	poetry run coverage run -m pytest
	poetry run coverage xml

package-install:
	poetry build
	python3 -m pip install --user dist/*.whl.

.PHONY: gendiff