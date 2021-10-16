"""Address generation prop for TrollFactory."""

from random import choice, randint
from json import loads
from pkgutil import get_data

COUNTRY_CODES = {'polish': 'PL', 'english_us': 'US'}


class Address:
    """Address generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Address generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies = ['language'] if 'language' not in \
            properties else []

    def generate(self) -> dict:
        """Generate the address."""
        language = self.properties['language']['language']

        if language == 'english_us':
            return {
                'prop_title': 'Address',
                'country_code': 'US',
                'address': 'Not available in US yet!',
            }

        region = choice(loads(get_data(
            __package__,
            'langs/'+self.properties['language']['language']+'/cities.json',
        )))

        country_state = region['region_name']

        for _ in range(10):
            city = choice(region['cities'])
            try:
                city_street = choice(city['streets'])
                break
            except (IndexError, KeyError):
                city_street = city['name']

        return {
            'prop_title': 'Address',
            'country_code': COUNTRY_CODES[language],
            'country_state': country_state,
            'country_city': city['name'],
            'city_postcode': city['postcode'],
            'city_street': city_street,
            'city_latitude': city['lat'],
            'city_longitude': city['lon'],
            'street_number': randint(1, 1000),
        }
