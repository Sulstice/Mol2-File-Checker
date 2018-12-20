#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# package setup
#
# ------------------------------------------------


# config
# ------
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# requirements
# ------------
with open('requirements.txt', 'r') as reqs:
    REQUIREMENTS = map(lambda x: x.rstrip(), reqs.readlines())

TEST_REQUIREMENTS = [
    'pytest',
    'pytest-runner'
]

MOL_2_CHECK = "Mol2Check"

# files
# -----
with open('README.md') as fi:
    README = fi.read()


# exec
# ----
setup(
    name=MOL_2_CHECK,
    version=MOL_2_CHECK.__version__,
    description=MOL_2_CHECK.__desc__,
    long_description=README,
    author=MOL_2_CHECK.__author__,
    author_email=MOL_2_CHECK.__email__,
    url=MOL_2_CHECK.__url__,
    packages=find_packages(include=[
        'mol2check',
    ]),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False,
    keywords=['mol2check', 'chemistry'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS
)
