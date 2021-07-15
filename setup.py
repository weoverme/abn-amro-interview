import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "abn-amro-interview-parser",
    version = "0.0.1",
    author = "Ray (Young Rae) Cho",
    author_email = "ray.cho94@hotmail.com",
    description = "Parses an input text file and outputs as a csv the Client information, Product information and Total Transaction Amount per Client per Product.",
    long_description = read("README.md"),
    url = "https://github.com/weoverme/abn-amro-interview",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    packages = [
        "src",
        "res",
        "log",
        "test"
    ]
)
