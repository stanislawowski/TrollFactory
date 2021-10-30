from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from trollfactory.props import measurements as prop


def test_generated_weight():
    assert prop.generate_weight(14) in range(37, 79)


def test_generated_height():
    assert prop.generate_height(16) in range(153, 190)


def test_generated_bmi():
    assert prop.generate_bmi(106, 161) == '40.89'


def test_generated_prop():
    assert prop.Measurements({'birthdate': {'age': 100}}).generate()
