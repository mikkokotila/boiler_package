#! /usr/bin/env python
#
# Copyright (C) 2019 Mikko Kotila

DESCRIPTION = "Boiler Package as an Example for Beginners"
LONG_DESCRIPTION = """\
This package provides a very simple example of how a minimal 
but still functional python package looks like.
"""

DISTNAME = 'boiler_package'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://github.com/mikkokotila/boiler_package'
LICENSE = 'MIT'
DOWNLOAD_URL = 'http://github.com/mikkokotila/boiler_package'
VERSION = '0.0.4'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

def check_dependencies():

    install_requires = []

    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')

    return install_requires


if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['boiler_package'],

          classifiers=[
                 'Intended Audience :: Science/Research',
                 'Programming Language :: Python :: 3.6',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],)
