from sys import path as spath
from os import path as opath
spath.append(opath.dirname(opath.dirname(opath.abspath(__file__))))
from trollfactory.props import address as prop

region_polish = prop.generate_region('polish')
city_polish = prop.generate_city(region_polish)


def test_generated_region():
    assert isinstance(prop.generate_region('polish'), dict)


def test_generated_country_state():
    assert isinstance(prop.generate_country_state(region_polish), str)


def test_generated_city():
    assert isinstance(city_polish, dict)


def test_generated_country_code():
    assert prop.generate_country_code('polish') == 'PL'


def test_generated_country_city():
    assert prop.generate_country_city(city_polish) == city_polish['name']


def test_generated_city_postcode():
    assert prop.generate_city_postcode(city_polish) == city_polish['postcode']


def test_generated_city_street():
    assert isinstance(prop.generate_city_street(city_polish), str)


def test_generated_city_latitude():
    assert prop.generate_city_latitude(city_polish) == city_polish['lat']


def test_generated_city_longitude():
    assert prop.generate_city_longitude(city_polish) == city_polish['lon']


def test_generated_street_number():
    assert isinstance(prop.generate_street_number(), int)


def test_generated_prop():
    assert prop.Address({'language': {'language': 'polish'}}).generate()
