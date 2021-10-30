from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from trollfactory.props import bank as prop


def test_generated_iban():
    assert len(prop.generate_iban('12400001')) == 34


def test_generated_prop():
    assert prop.Bank({'language': {'language': 'polish'},
                      'birthdate': {'age': 20}}).generate()


def test_no_bank_account_under_13():
    assert prop.Bank({'language': {'language': 'polish'},
                      'birthdate': {'age': 10}}).generate() is None
