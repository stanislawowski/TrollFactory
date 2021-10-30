from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from trollfactory.props import name as prop


def test_generated_name():
    assert isinstance(prop.generate_name('polish', 'female'), str)


def test_generated_surname():
    assert isinstance(prop.generate_surname('polish', 'male'), str)


def test_generated_prop():
    assert prop.Name({'language': {'language': 'polish'},
                      'gender': {'gender': 'non-binary'}}).generate()
