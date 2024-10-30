from setuptools import setup

setup(
    name='tex_cleaner',
    version='0.1',
    install_requires=['git+https://github.com/SL2000s/lm_theory.git', 'lunarcore @ git+https://github.com/lunarbase-ai/lunar.git@lunarbase#subdirectory=lunarbase/core'],
    tests_require=['pytest'],
    extras_require={'dev': ['pytest']},
    author='Lunarbase (https://lunarbase.ai/)',
    author_email='contact@lunarbase.ai',
    description='Cleans up Latex codes a by removing its comments and expanding its restatables.',
    license='SPDX-License-Identifier: GPL-3.0-or-later',
)
