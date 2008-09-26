from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='doctestpdbhacks',
      version=version,
      description="pdb doesn't play nice with doctests..  this is a quick hack to fix that.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jordan Baker',
      author_email='jbb AT scryent DOT com',
      url='http://scryent.com',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
