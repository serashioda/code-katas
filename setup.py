"""The setup for katas modules."""

from setuptools import setup

setup(
    name="code katas",
    description="A Python implementation of Code War katas..",
    version=0.1,
    author="Sera Smith",
    author_email="seras37@gmail.com",
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['','','','','','','','',''],
    install_requires=['numpy', 'tox'],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov", 'tox']
    },
)
