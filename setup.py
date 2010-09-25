from setuptools import setup, find_packages
import sys, os

version = '0.2.1'

setup(name='xychan',
      version=version,
      description="A 'chan-style' web message board similar to Wakaba",
      long_description=open('README.md', 'r').read(),
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Communications :: BBS",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='4chan, chan, message board, Wakaba',
      author='Mike Verdone',
      author_email='mike.verdone@gmail.com',
      url='http://mike.verdone.ca/xychan',
      license='GNU General Public License v3 (GPL)',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'bottle>=0.8.3',
          'sqlalchemy>=0.6',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
