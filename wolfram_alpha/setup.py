from setuptools import setup

setup(
    name='wolfram_alpha',
    version='0.1',
    install_requires=['wolframalpha==5.0.0', 'lunarcore @ git+https://github.com/lunarbase-ai/lunar.git@lunarbase#subdirectory=lunarbase/core'],
    tests_require=['pytest'],
    extras_require={'dev': ['pytest']},
    author='Lunarbase (https://lunarbase.ai/)',
    author_email='contact@lunarbase.ai',
    description='Obtains a response from the WolframAlpha API.',
    license='SPDX-License-Identifier: GPL-3.0-or-later',
)
