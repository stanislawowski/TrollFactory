from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from uuid import UUID
from trollfactory.props import phone as prop


def test_generated_phone():
    assert isinstance(prop.generate_phone('polish'), dict)


def test_generated_phone_brand():
    assert prop.generate_phone_brand({'brand': 'Samsuwung'}) == 'Samsuwung'


def test_generated_phone_model():
    assert prop.generate_phone_model({'model': 'Nya A1'}) == 'Nya A1'


def test_generated_phone_operator():
    assert isinstance(prop.generate_phone_operator('polish'), str)


def test_generated_phone_number():
    assert int(prop.generate_phone_number('polish', 'Orange').replace('+', ''))


def test_generated_phone_operating_system():
    assert prop.generate_phone_operating_system({'os': '👍🏿'}) == '👍🏿'


def test_generated_phone_uuid():
    assert UUID(prop.generate_phone_uuid())


def test_generated_receive_sms_url():
    assert prop.generate_receive_sms_url().startswith('http')


def test_generated_send_sms_url():
    assert prop.generate_send_sms_url().startswith('http')


def test_generated_phone_call_url():
    assert prop.generate_phone_call_url().startswith('http')


def test_generated_prop():
    assert prop.Phone({'language': {'language': 'polish'}}).generate()
