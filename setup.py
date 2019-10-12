#!/usr/bin/env python
"""
@author: metalcorebear
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NRCLex",
    version="0.0.1",
    author="Mark M. Bailey",
    author_email="mark.mbailey@gmail.com",
    description="An affect generator based on TextBlob and the NRC affect lexicon.  Note that lexicon license is for research purposes only.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/metalcorebear/NRCLex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)