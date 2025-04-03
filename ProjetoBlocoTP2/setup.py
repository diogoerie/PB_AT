from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("soma_paralela.pyx", compiler_directives={'language_level': "3"})
)
