#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="ipsexamples",
    version="0.1.0",
    install_requires=[
        'ipsframework==0.2.0'
    ],
    packages=find_packages()
)
