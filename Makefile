build:
	flake8 detransliterator --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	flake8 tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	rm -rf dist
	hatch build

test:
	pytest -s

publish:
	hatch publish