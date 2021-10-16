from re import match
from trollfactory.props.address import Address

generated_address = Address({'language': {'language': 'polish'}}).generate()


def test_address_generated():
    assert generated_address['prop_title'] == 'Address'


def test_country_code():
    assert generated_address['country_code'] == 'PL'


def test_country_state_generated():
    assert isinstance(generated_address['country_state'], str)


def test_country_city_generated():
    assert isinstance(generated_address['country_city'], str)


def test_city_postcode_format():
    assert match('^\\d{2}[- ]{0,1}\\d{3}$', generated_address['city_postcode'])


def test_city_street_generated():
    assert isinstance(generated_address['city_street'], str)


def test_city_latitude_format():
    assert float(generated_address['city_latitude'])


def test_city_longitude_format():
    assert float(generated_address['city_longitude'])


def test_street_number_format():
    assert generated_address['street_number'] in range(1, 1000)
