from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='xychan',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Mike Verdone',
      author_email='mike.verdone@gmail.com',
      url='http://mike.verdone.ca/xychan',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          'bottle',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
