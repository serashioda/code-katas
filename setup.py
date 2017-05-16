"""The setup for katas modules."""

from setuptools import setup

setup(
    name="code katas",
    description="A Python implementation of Code War katas",
    version=0.1,
    author="Sera Smith",
    author_email="seras37@gmail.com",
    license='MIT',
    py_modules=['calculate_years', 'count_bits', 'decending_order', 'find_odd_int', 'human_readable', 'is_isogram', 'multiply', 'parenthetics', 'remove_min', 'shortest_word', 'sort_cards', 'string_pyramid', 'sum_terms' 'xo'],
    package_dir={'': 'src'},
    install_requires=['numpy', 'tox'],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov", 'tox']
    },
)
