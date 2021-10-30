from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from trollfactory.props import document_id as prop


def test_generated_id_number():
    assert isinstance(prop.generate_id_number('polish'), str)


def test_generated_expiry_date():
    assert len(prop.generate_expiry_date('polish').split('/')) == 3


def test_generated_prop():
    assert prop.DocumentId({'language': {'language': 'polish'}}).generate()
