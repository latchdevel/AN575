"""
Python module to convert between Microchip's 32/24-bit float format 
as described in AN575 and standart IEEE-754 32-bit format.

See: https://github.com/latchdevel/AN575

Copyright (c) 2023 Jorge Rivera. All right reserved.
License GNU Lesser General Public License v3.0.
"""

from setuptools import setup

setup(
    name="AN575",
    version="1.0.0",
    packages=["AN575","AN575.tests"],
    url="https://github.com/latchdevel/AN575",
    author="Jorge Rivera",
    author_email="latchdevel@users.noreply.github.com",
    description='Converts between Microchip AN575 float format and standart IEEE-754',
    long_description=open("README.md", 'r').read(),
    long_description_content_type="text/markdown",
    keywords="AN575, IEEE-754, IEEE754, float, format, Microchip, PIC, PICmicro, PIC16, PIC17, PIC18",
    license='LGPL-3.0',
    license_files=["LICENSE.txt"],
    classifiers=[ # https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "Operating System :: OS Independent"
    ],
    platforms=["any"],
    test_suite = 'AN575.tests'
)
