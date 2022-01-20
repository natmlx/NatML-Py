# 
#   NatML
#   Copyright (c) 2022 Yusuf Olokoba.
#

from os import path, walk
from setuptools import find_packages, setup

# Get readme
with open("README.md", "r") as readme:
    long_description = readme.read()

# Get version
with open("natml/version.py") as version_source:
    gvars = {}
    exec(version_source.read(), gvars)
    version = gvars["__version__"]

# Load template data
def package_files(directory):
    paths = []
    for file_path, _, filenames in walk(directory):
        for filename in filenames:
            paths.append(path.join("..", file_path, filename))
    return paths
template_data = package_files("natml/cli/templates")

# Setup
setup(
    name="natml",
    version=version,
    author="NatML",
    author_email="hi@natml.ai",
    description="Zero deployment machine learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
	python_requires=">=3.6",
    install_requires=[
        "numpy",
        "path",
        "Pillow",
        "pyyaml"
    ],
    url="https://natml.ai",
    packages=find_packages(
        include=["natml", "natml.*"],
        exclude=["test", "examples"]
    ),
    package_data={
        "": template_data
    },
    entry_points={
        "console_scripts": [
            "natml=natml.cli.__init__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Documentation": "https://docs.natml.ai/python",
        "Source": "https://github.com/natsuite/NatML-Py"
    },
)