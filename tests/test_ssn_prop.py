from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from trollfactory.props import ssn as prop


def test_generated_ssn():
    assert prop.generate_ssn('polish', 'male', 1900, 1, 1).startswith('000101')


def test_generated_prop():
    assert prop.Ssn({'language': {'language': 'polish'},
                     'gender': {'gender': 'non-binary'},
                     'birthdate': {'birth_year': 1900, 'birth_month': 1,
                                   'birth_day': 1}}).generate()
