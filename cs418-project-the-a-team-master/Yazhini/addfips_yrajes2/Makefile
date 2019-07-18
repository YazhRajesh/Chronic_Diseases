# This file is part of addfips.
# http://github.com/fitnr/addfips

# Licensed under the GPL-v3.0 license:
# http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2016, fitnr <fitnr@fakeisthenewreal>

.PHONY: test cov

cov: | test
	coverage html

test:
	coverage run --include=addfips/* setup.py test

deploy: README.rst
	python setup.py register
	git push; git push --tags
	rm -rf dist build
	python3 setup.py bdist_wheel --universal
	twine upload dist/*

README.rst: README.md
	- pandoc $< -o $@
	@touch $@
	python setup.py check -r -s -m -q
