"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Setup file for the hello_world package.
"""

from setuptools import find_packages, setup

setup(
    name="my-hello-world",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python package that prints 'Hello, World!'",
    long_description=open("readme.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hello_world",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
