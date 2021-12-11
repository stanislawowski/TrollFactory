from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from trollfactory.props import cc as prop
from luhn import verify


def test_generated_americanexpress():
    number = str(prop.generate_card_number('americanexpress'))
    assert len(number) == 15 and verify(number)


def test_generated_diners():
    number = str(prop.generate_card_number('diners'))
    assert len(number) == 14 and verify(number)


def test_generated_discover():
    number = str(prop.generate_card_number('discover'))
    assert len(number) == 16 and verify(number)


def test_generated_jcb():
    number = str(prop.generate_card_number('jcb'))
    assert len(number) == 16 and verify(number)


def test_generated_mastercard():
    number = str(prop.generate_card_number('mastercard'))
    assert len(number) == 16 and verify(number)


def test_generated_visa():
    number = str(prop.generate_card_number('visa'))
    assert len(number) == 16 and verify(number)


def test_generated_cvv3():
    assert len(str(prop.generate_cvv3())) == 3


def test_generated_cvv4():
    assert len(str(prop.generate_cvv4())) == 4


def test_generated_expiry_date():
    assert [int(i) for i in prop.generate_expiry_date().split('/')]


def test_generated_prop():
    assert prop.Cc({'birthdate': {'age': 20}, 'name': {
        'name': 'Marcin', 'surname': 'Kowal'}}).generate()


def test_no_cc_under_18():
    assert prop.Cc({'birthdate': {'age': 10}, 'name': {
        'name': 'Marcin', 'surname': 'Kowal'}}).generate() is None
