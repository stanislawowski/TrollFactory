from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from trollfactory.props import language as prop


def test_generated_language():
    assert prop.Language({'language': {'language': 'polish'}}
                         ).generate()['language'] == 'polish'


def test_generated_prop():
    assert prop.Language({'language': {'language': 'polish'}}).generate()
