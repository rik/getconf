#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2010-2015 Polyconseil SAS
# This software is distributed under the two-clause BSD license.
from __future__ import unicode_literals
import io
import os
import re

from setuptools import setup

root_dir = os.path.abspath(os.path.dirname(__file__))


def get_version(package_name):
    version_re = re.compile(r"^__version__ = [\"']([\w_.-]+)[\"']$")
    package_components = package_name.split('.')
    init_path = os.path.join(root_dir, *(package_components + ['__init__.py']))
    with io.open(init_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = version_re.match(line[:-1])
            if match:
                return match.groups()[0]
    return '0.1.0'


def get_long_description(filename):
    with io.open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    return text


def get_requirements(filename):
    with io.open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()


PACKAGE = 'getconf'

setup(
    name=PACKAGE,
    version=get_version(PACKAGE),
    description="getconf, a versatile configuration lib for Python projects",
    long_description=get_long_description('README.rst'),
    author="Polyconseil",
    author_email="opensource+%s@polyconseil.fr" % PACKAGE,
    license="BSD",
    keywords=['configuration', 'environment', 'setup', 'getconf', 'config'],
    url="https://github.com/Polyconseil/%s/" % PACKAGE,
    download_url="https://pypi.python.org/pypi/%s/" % PACKAGE,
    packages=[PACKAGE],
    platforms=["OS Independent"],
    install_requires=get_requirements('requirements.txt'),
    setup_requires=[
        'setuptools>=0.8',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Systems Administration",
    ],
    test_suite='tests',
)
