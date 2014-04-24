
help:
	@echo "keywords that can be used: rpm clean"

rpm:
	python setup.py bdist_rpm

clean:
	python setup.py clean
	rm -rvf dist/* *egg-info build/*
