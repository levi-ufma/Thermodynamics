"""
    Mu to temperature python package

    See:
        https://github.com/Levi-UFMA
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'readme.md'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='Mu-to-temperature',
    version='0.1.0',
    description='calculates a temperature estimate corresponding to the chemical potential supplied by the user',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Levi-UFMA/utils',
    author='LEVI',
    author_email='levi@email.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['texts']),
    install_requires=[
        'matplotlib',
        'numpy',
        'pymatgen',
    ]
)
