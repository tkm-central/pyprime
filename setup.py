# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyprime',
    version='0.0.1',
    description='Python packege for probabilistic primarity test',
    long_description=readme,
    author='tkm',
    author_email='unknown',
    install_requires=['numpy'],
    url='https://github.com/tkm-central/pyprime',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
    test_suite='tests'
)

