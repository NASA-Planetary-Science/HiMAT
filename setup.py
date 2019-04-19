#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

#To prepare a new release
#python setup.py sdist upload

setup(name='himatpy',
    version='0.1.0',
    description='Libraries and command-line utilities for HiMAT',
    author='Anthony Arendt',
    author_email='arendta@uw.edu',
    license='MIT',
    url='https://github.com/NASA-Planetary-Science/HiMAT',
    packages=['himatpy', 'himatpy.GRACE_MASCON', 'himatpy.LIS', 'himatpy.MODSCAG', 'himatpy.tools'],
    long_description=open('README.md').read(),
    #install_requires=['gdal','numpy','scipy','matplotlib'],
    #Note: this will write to /usr/local/bin
    scripts=['himatpy/modscag_download.py', 'himatpy/LIS/LISpreprocess.py']
)
