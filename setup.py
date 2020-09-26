#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="hangman",
    version="0.0.0",
    author="Alexander Proskurin",
    author_email="whitestoic@gmail.com",
    url="https://github.com/GhostPandaGP/hangman",
    license="MIT",
    packages=[
        "hangman",
    ],
    install_requires=[
        "pylint",
        "pytest",
        "pep257",
        "pycodestyle"
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-cov",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-pylint"
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ]
)
