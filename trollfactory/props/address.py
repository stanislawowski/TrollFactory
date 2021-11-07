"""Address generation prop for TrollFactory."""

from random import choice, randint
from typing import Any, TypedDict
from json import loads
from pkgutil import get_data

COUNTRY_CODES: dict[str, str] = {'polish': 'PL', 'english_us': 'US'}


class AddressType(TypedDict):
    """Type hint for an address property."""

    prop_title: str
    country_code: str
    country_state: str
    country_city: str
    city_postcode: str
    city_street: str
    city_latitude: float
    city_longitude: float
    street_number: int



def generate_region(language: str) -> dict[str, Any]:
    """Generate a dict with region data."""
    return choice(loads(get_data(
        __package__, 'langs/'+language+'/cities.json')))


def generate_country_state(region: dict) -> str:
    """Generate a region name."""
    return region['region_name']


def generate_city(region: dict) -> dict[str, Any]:
    """Generate a dict with city data."""
    return choice(region['cities'])


def generate_country_code(language: str) -> str:
    """Generate a country code."""
    return COUNTRY_CODES[language]


def generate_country_city(city: dict) -> str:
    """Generate a city name."""
    return city['name']


def generate_city_postcode(city: dict) -> str:
    """Generate a postcode."""
    return city['postcode']


def generate_city_street(city: dict) -> str:
    """Generate a street name."""
    return choice(city['streets'])


def generate_city_latitude(city: dict) -> float:
    """Generate a latitude."""
    return city['lat']


def generate_city_longitude(city: dict) -> float:
    """Generate a longitude."""
    return city['lon']


def generate_street_number() -> int:
    """Generate a street number."""
    # TODO: check if this street number actually exists
    return randint(1, 1000)


class Address:
    """Address generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = ['language'] if 'language' \
            not in properties else []

    def generate(self) -> AddressType:
        """Generate the address data."""
        # Used properties
        language: str = self.properties['language']['language']

        # TODO: finish the english_us dataset and remove this
        if language == 'english_us':
            return {'prop_title': 'Address', 'country_code': 'US'}

        # Generate data
        region: dict[str, Any] = generate_region(language)
        country_state: str = generate_country_state(region)
        city: dict[str, Any] = generate_city(region)
        city_street: str = generate_city_street(city)
        country_code: str = generate_country_code(language)
        country_city: str = generate_country_city(city)
        city_postcode: str = generate_city_postcode(city)
        city_latitude: float = generate_city_latitude(city)
        city_longitude: float = generate_city_longitude(city)
        street_number: int = generate_street_number()

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
