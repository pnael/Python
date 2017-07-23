#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My project',
    'author': 'Philippe Naël',
    'url': 'URL to get it at',
    'download url': 'Where to download it',
    'author_email': 'philippe.nael@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'script': [],
    'name': 'projectname'
}

setup(**config)
