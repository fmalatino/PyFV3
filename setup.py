#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_namespace_packages, setup


with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

requirements = [
    "f90nml>=1.1.0",
    "numpy==1.21.2",
    "xarray",
]

test_requirements = ["pytest", "pytest-subtests", "serialbox", "coverage"]
ndsl_requirements = ["ndsl @ git+https://github.com/fmalatino/NDSL.git@benchmark_freeze"]
develop_requirements = test_requirements + ndsl_requirements + ["pre-commit"]

extras_requires = {
    "test": test_requirements,
    "ndsl": ndsl_requirements,
    "develop": develop_requirements,
}

setup(
    author="The Allen Institute for Artificial Intelligence",
    author_email="oliver.elbert@noaa.gov",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="pyFV3 is a NDSL-based FV3 dynamical core for atmospheric models",
    install_requires=requirements,
    extras_require=extras_requires,
    license="BSD license",
    long_description=readme,
    include_package_data=True,
    name="pyFV3",
    packages=find_namespace_packages(include=["pyFV3", "pyFV3.*"]),
    setup_requires=[],
    test_suite="tests",
    url="https://github.com/NOAA-GFDL/pyFV3",
    version="0.2.0",
    zip_safe=False,
)
