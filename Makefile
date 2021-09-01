# BGE 开放平台 Makefile 工具

PYTHON=`which python`

install:
	$(PYTHON) setup.py install

# 构建源码包
build: wheel
	$(PYTHON) setup.py build sdist

# 构建 wheel 包
wheel:
	$(PYTHON) setup.py bdist_wheel

clean:
	rm -rf build dist *.egg-info __pycache__ \
		   bgesdk/__pycache__ bgesdk/*.pyc bgesdk/management/*.pyc \
		   bgesdk/commands/*.pyc tests/__pycache__ tests/*.pyc

.PHONY: build wheel install clean
