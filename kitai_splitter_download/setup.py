from setuptools import setup

setup(
    name='kitai_splitter_download',
    version='0.1',
    install_requires=['lunarcore @ git+https://github.com/lunarbase-ai/lunar.git@lunarbase#subdirectory=lunarbase/core'],
    tests_require=['pytest'],
    extras_require={'dev': ['pytest']},
    author='Lunarbase (https://lunarbase.ai/)',
    author_email='contact@lunarbase.ai',
    description='Download the result of a split opperation from Kits.ai',
    license='SPDX-License-Identifier: GPL-3.0-or-later',
)
