#!/usr/bin/env python

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup


setup(name='genderize',
      version='0.1.1',
      license='MIT',
      description='Genderize tries to infer gender information looking at first name and/or making text analysis',
      long_description=open('README.md').read(),
      url='https://github.com/muatik/genderize',
      author='Mustafa Atik',
      author_email='muatik@gmail.com',
      maintainer='Mustafa Atik',
      maintainer_email='muatik@gmail.com',
      packages=['genderize'],
      platforms='any')