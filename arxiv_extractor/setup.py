from setuptools import setup

setup(
    name='arxiv_extractor',
    version='0.1',
    install_requires=['git+https://github.com/SL2000s/lm_theory.git', 'lunarcore @ git+https://github.com/lunarbase-ai/lunar.git@lunarbase#subdirectory=lunarbase/core'],
    tests_require=['pytest'],
    extras_require={'dev': ['pytest']},
    author='Lunarbase (https://lunarbase.ai/)',
    author_email='contact@lunarbase.ai',
    description='Extracts titles, authors, latex code, etc. of Arxiv papers.',
    license='SPDX-License-Identifier: GPL-3.0-or-later',
)
