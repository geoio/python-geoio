#!/usr/bin/env python
from setuptools import setup

setup(name='python-geoio',
      version='0.1',
      description='Python bindings for the geo.io API.',
      author='Felix Wittmann',
      author_email='felix@geo.io',
      url='http://geo.io',
      packages=['geoio'],
      license='BSD License',
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: GIS',
          'Topic :: Internet'
      ],
      use_2to3=True,
      )