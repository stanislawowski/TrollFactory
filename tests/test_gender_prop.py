from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from trollfactory.props import gender as prop


def test_generated_gender():
    assert prop.Gender({'gender': {'gender': 'female'}}
                       ).generate()['gender'] == 'female'


def test_generated_prop():
    assert prop.Gender({'gender': {'gender': 'non-binary'}}).generate()
