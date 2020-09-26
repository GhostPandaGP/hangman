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
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-cov",
        "pycodestyle",
        "pep257",
        "pylint"
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
