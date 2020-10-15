#!/usr/bin/env python

# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re
import os
import codecs

name = 'python-lfu'
package = 'lfu_cache'
description = 'A Python LFU cache implementation with O(1) eviction scheme'
url = 'https://github.com/psykidellic/python-lfu'
author = 'Ritesh Nadhani'
author_email = 'riteshn@gmail.com'
license = 'Unilicense'
install_requires = []
extras_require = {}

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = codecs.open(os.path.join(package, '__about__.py'), encoding='utf-8').read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)

EXCLUDE_FROM_PACKAGES = []

setup(
    name=name,
    version=get_version(package),
    url=url,
    license=license,
    description=description,
    long_description=description,
    author=author,
    author_email=author_email,
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires='>=3.6',
    classifiers=classifiers,
)
