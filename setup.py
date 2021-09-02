# coding: utf-8

"""
    NHL API

    Documenting the publicly accessible portions of the NHL API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
# Always prefer setuptools over distutils
# To use a consistent encoding
from codecs import open
from os import path
from setuptools import setup, find_packages  # noqa: H301

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

NAME = "powerplay"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", 
            "six >= 1.10", 
            "certifi", 
            "python-dateutil",
            'numpy>=1.13.0',
            'pandas >= 1.0.3',
            'beautifulsoup4>=4.4.0',
            'requests>=2.18.1',
            'lxml>=4.2.1',
            'pyarrow>=1.0.1',
            'pygithub>=1.51',
            'scipy>=1.4.0',
            'matplotlib>=2.0.0',
            'tqdm>=4.50.0',
            'attrs>=20.3.0']

setup(
    name=NAME,
    version=VERSION,
    description="Functions to Access Hockey Play by Play Data from the NHL API",
    # Author details
    author='Saiem Gilani',
    author_email='saiem.gilani@gmail.com',

    # Maintainer
    maintainer='Saiem Gilani',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    url="http://www.github.com/saiemgilani/powerplay",

    # What does your project relate to?
    keywords=["Swagger", "NHL API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=long_description
)