# Makefile for maintainer tasks

dist:
	tox && \
	git diff --exit-code && \
	rm -rf ./dist && \
	mkdir dist && \
	python -m build

release: dist
	twine upload dist/* && \
	git tag v$$(python3 setup.py --version) && \
	git push --tags
