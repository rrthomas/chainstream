# Makefile for maintainer tasks

dist:
	tox && \
	git diff --exit-code && \
	rm -rf ./dist && \
	mkdir dist && \
	python -m build

release: dist
	twine upload dist/* && \
	git tag v$$(grep version pyproject.toml | grep -o "[0-9.]\+") && \
	git push --tags

.PHONY:	dist
