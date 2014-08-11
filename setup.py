#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="opencivicdata-api",
      version='0.0.1',
      author="Paul Tagliamonte",
      author_email='paultag@sunlightfoundation.com',
      license="BSD-3",
      description="python opencivicdata api wrapper",
      long_description="",
      url="",
      packages=['opencivicdata.api',],
      include_package_data=True,
      platforms=["any"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   ],
      )
