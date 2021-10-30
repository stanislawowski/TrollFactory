"""Setup file for TrollFactory."""

from setuptools import setup

VERSION: str = '2.1.2'
DESCRIPTION: str = 'Fake personality generator for the 21st century!'

with open('README.md', encoding='utf-8') as file:
    LONG_DESCRIPTION: str = file.read()

setup(
    name='trollfactory',
    version=VERSION,
    author='Stanisławowski Research & Development',
    author_email='<office@stanislawowski.pl>',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=['trollfactory'],
    install_requires=['schwifty'],
    keywords=['fake', 'personality', 'personalities', 'generator'],
    entry_points={
        'console_scripts': [
            'trollfactory = trollfactory.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    include_package_data=True,
)
