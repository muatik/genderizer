#!/usr/bin/env python

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup


setup(name='genderizer',
      version='0.1.2.3',
      license='MIT',
      description='Genderizer tries to infer gender information looking at first name and/or making text analysis',
      long_description=open('README.md').read(),
      url='https://github.com/muatik/genderizer',
      author='Mustafa Atik',
      author_email='muatik@gmail.com',
      maintainer='Mustafa Atik',
      maintainer_email='muatik@gmail.com',
      packages=['genderizer'],
      package_data={'genderizer': ['data/*']},
      platforms='any')