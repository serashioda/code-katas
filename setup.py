"""The setup for katas modules."""

from setuptools import setup

setup(
    name="code katas",
    description="A Python implementation of Code War katas",
    version=0.1,
    author="Sera Smith",
    author_email="seras37@gmail.com",
    license='MIT',
    py_modules=['calculate_years', 'count_bits', 'decending_order', 'find_odd_int', 'is_isogram', 'multiply', 'remove_min', 'shortest_word', 'xo'],
    package_dir={'': 'src'},
    install_requires=['numpy', 'tox'],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov", 'tox']
    },
)
