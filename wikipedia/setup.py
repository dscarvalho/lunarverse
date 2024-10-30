from setuptools import setup

setup(
    name='wikipedia',
    version='0.1',
    install_requires=['wikipedia==1.4.0', 'lunarcore @ git+https://github.com/lunarbase-ai/lunar.git@lunarbase#subdirectory=lunarbase/core'],
    tests_require=['pytest'],
    extras_require={'dev': ['pytest']},
    author='Lunarbase (https://lunarbase.ai/)',
    author_email='contact@lunarbase.ai',
    description='Retrieves data from Wikipedia API.',
    license='SPDX-License-Identifier: GPL-3.0-or-later',
)
