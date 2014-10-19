#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2013 by S. Andrew Sheppard
    :contact: andrew@wq.io
"""


from setuptools import setup
from os.path import join, dirname

LONG_DESCRIPION = """
Webhooks for GitHub post-receive hooks and other POST requests.
"""

def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(
    name='threebot-hook',
    version='0.1.0',
    description='GitHub (& Bitbucket) web hooks for 3bot',
    long_description=long_description(),
    author='arteria GmbH',
    author_email='admin@arteria.ch',
    packages = ['threebot_hook'],
    install_requires=['Django', 'djangorestframework'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta',
    ],
    test_suite='tests'
)
