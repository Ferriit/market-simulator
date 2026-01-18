from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

setup(
    ext_modules=[
        Pybind11Extension(
            "sim",
            ["src/sim.cpp"],
        ),
    ],
)

