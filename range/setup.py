from setuptools import setup

setup(
    name='range',
    version='0.1',
    install_requires=['lunarcore @ git+https://github.com/lunarbase-ai/lunar.git@lunarbase#subdirectory=lunarbase/core'],
    tests_require=['pytest'],
    extras_require={'dev': ['pytest']},
    author='Lunarbase (https://lunarbase.ai/)',
    author_email='contact@lunarbase.ai',
    description='Generate a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.',
    license='SPDX-License-Identifier: GPL-3.0-or-later',
)
