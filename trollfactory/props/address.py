"""Address generation prop for TrollFactory."""

from random import choice, randint
from json import loads
from pkgutil import get_data

COUNTRY_CODES = {'polish': 'PL', 'english_us': 'US'}


def generate_region(language: str) -> dict:
    return choice(loads(get_data(
        __package__, 'langs/'+language+'/cities.json')))


def generate_country_state(region: dict) -> str:
    return region['region_name']


def generate_city(region: dict) -> dict:
    while True:
        city = choice(region['cities'])
        # check if the city contains any streets
        if 'streets' in city and len(city['streets']):
            return city


def generate_country_code(language: str) -> str:
    return COUNTRY_CODES[language]


def generate_country_city(city: dict) -> str:
    return city['name']


def generate_city_postcode(city: dict) -> str:
    return city['postcode']


def generate_city_street(city: dict) -> str:
    return choice(city['streets'])


def generate_city_latitude(city: dict) -> float:
    return city['lat']


def generate_city_longitude(city: dict) -> float:
    return city['lon']


def generate_street_number() -> int:
    # TODO: check if this street number actually exists
    return randint(1, 1000)


class Address:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies = ['language'] if 'language' not in \
            properties else []

    def generate(self) -> dict:
        # Used properties
        language = self.properties['language']['language']

        # TODO: finish the english_us dataset and remove this
        if language == 'english_us':
            return {'prop_title': 'Address', 'country_code': 'US'}

        # Generate data
        region = generate_region(language)
        country_state = generate_country_state(region)
        city = generate_city(region)
        city_street = generate_city_street(city)
        country_code = generate_country_code(language)
        country_city = generate_country_city(city)
        city_postcode = generate_city_postcode(city)
        city_latitude = generate_city_latitude(city)
        city_longitude = generate_city_longitude(city)
        street_number = generate_street_number()

        return {
            'prop_title': 'Address',
            'country_code': country_code,
            'country_state': country_state,
            'country_city': country_city,
            'city_postcode': city_postcode,
            'city_street': city_street,
            'city_latitude': city_latitude,
            'city_longitude': city_longitude,
            'street_number': street_number,
        }
