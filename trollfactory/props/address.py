from random import choice, randint
from json import loads
from pkgutil import get_data

COUNTRY_CODES = {
    'polish': 'PL',
    'english_us': 'US',
}


class Address:
    depedencies = ["language"]

    def generate(properties):
        if properties['language']['language'] == 'english_us':
            return {
                'prop_title': 'Address',
                'country_code': 'US',
                'address': 'Not available in US yet!',
            }

        region = choice(loads(get_data(
            __package__,
            'langs/' + properties['language']['language'] + '/cities.json',
        )))

        country_state = region['region_name']

        for i in range(10):
            city = choice(region['cities'])
            try:
                city_street = choice(city['streets'])
                break
            except (IndexError, KeyError):
                city_street = city['name']

        return {
            'prop_title': 'Address',
            'country_code': COUNTRY_CODES[properties['language']['language']],
            'country_state': country_state,
            'country_city': city['name'],
            'city_postcode': city['postcode'],
            'city_street': city_street,
            'city_latitude': city['lat'],
            'city_longitude': city['lon'],
            'street_number': randint(1, 1000),
        }
