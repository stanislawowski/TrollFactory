from setuptools import setup

VERSION = '2.0.0'
DESCRIPTION = 'Fake personality generator for the 21st century!'

setup(
    name = 'trollfactory',
    version = VERSION,
    author = 'Stanisławowski Research & Development',
    author_email = '<office@stanislawowski.pl>',
    description = DESCRIPTION,
    long_description = DESCRIPTION,
    packages = ['trollfactory'],
    install_requires = ['schwifty'],
    keywords = ['fake', 'personality', 'personalities', 'generator'],
    entry_points = {
        'console_scripts': [
            'trollfactory = trollfactory.cli:main'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    include_package_data = True
)
