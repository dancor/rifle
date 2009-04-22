#!/usr/bin/env python
from setuptools import setup

setup(
    name='rifle',
    version='1.2',
    description='interactively tag sound file segments',
    author='Chris Putnam',
    author_email='chrisputnam@gmail.com',
    url='http://www.facebook.com/profile.php?id=13',
    packages=['rifle'],
    package_dir={'rifle': 'src'},
    package_data={'rifle': []},
    scripts=['src/rifle'],
    data_files=[],
    install_requires=[],
)
