from distutils.core import Extension

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt') as fh:
    requirements = [line.strip() for line in fh.readlines()]

_DEBUG = False

if _DEBUG:
    extra_compile_args = ['/DEBUG']
else:
    extra_compile_args = []

setuptools.setup(
    name='pazzle-game',
    version='0.0.1',
    author='15PuzzleGame',
    author_email='pishenkovladyslav@gmail.com',
    description='Library to play scalable PuzzleGame.',
    install_requires=requirements,
    packages=setuptools.find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
