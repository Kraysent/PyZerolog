push-pypi: 
	rm -rf dist
	python3 setup.py sdist
	twine upload dist/*

install:
	pip install .