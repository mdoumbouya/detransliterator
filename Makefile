build:
	rm -rf dist
	hatch build

publish:
	hatch publish