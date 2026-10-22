VERSION ?= Version de développement
.PHONY: build check clean
check:
	python3 scripts/check_project.py
build: check
	bash scripts/build.sh "$(VERSION)"
clean:
	rm -rf dist
