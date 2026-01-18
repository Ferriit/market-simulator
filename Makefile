PYTHON=python3
VENV=venv
MODULE_DIR=src/modules

all: sim

sim:
	$(PYTHON) build/setup.py build_ext --inplace
	mkdir -p $(MODULE_DIR)
	mv sim.cpython*.so $(MODULE_DIR)/sim.so
	touch src/modules/__init__.py

install:
	[ -d $(VENV) ] || $(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip pybind11
