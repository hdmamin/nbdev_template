SRC = $(wildcard notebooks/*.ipynb)

todo:
	ack -R 'TODO' {bin,lib,notebooks,dev_notebooks,notes,reports,services} || :

clean:
	nbdev_clean_nbs

lib:
	nbdev_build_lib
	touch {{cookiecutter.dir_name}}

dist: lib
	rm -rf dist && python setup.py sdist bdist_wheel
			 
pypi: dist
	cd lib && twine upload --repository pypi dist/*
	
docs: $(SRC)
	nbdev_build_docs
	touch docs

docs_serve: docs
	cd docs && bundle exec jekyll serve --livereload

all: lib docs
