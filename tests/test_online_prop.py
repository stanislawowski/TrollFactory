from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from re import match
from trollfactory.props import online as prop


def test_generated_username():
    assert 'eee' in prop.generate_username('ddd', 'eee')


def test_generated_email():
    assert match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
                 prop.generate_email('aaa', 'polish'))


def test_generated_email_url():
    assert prop.generate_email_url('@niepodam.pl', 'ddd') \
        == 'http://niepodam.pl/users/ddd'


def test_generated_domain_name():
    assert 'asdf.' in prop.generate_domain_name('asdf')


def test_generated_password():
    assert len(prop.generate_password()) >= 16


def test_generated_setup():
    assert isinstance(prop.generate_setup('polish'), dict)


def test_generated_operating_system():
    assert prop.generate_operating_system({'os': 'Uwubuntu'}) == 'Uwubuntu'


def test_generated_browser():
    assert prop.generate_browser({'browser': 'Furfox'}) == 'Furfox'


def test_generated_user_agent():
    assert prop.generate_user_agent({'user_agent': ['a', 'a', 'a']}) == 'a a a'


def test_generated_ipv4():
    ipv4 = prop.generate_ipv4().split('.')
    assert len(ipv4) == 4 and [int(i) for i in ipv4]


def test_generated_ipv6():
    assert len(prop.generate_ipv6().split(':')) == 8


def test_generated_mac():
    assert len(prop.generate_mac().split(':')) == 6


def test_generated_prop():
    assert prop.Online({'language': {'language': 'polish'},
                        'name': {'name': 'hhh', 'surname': 'HHH'}}).generate()
