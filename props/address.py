from random import choice, randint
from json import load

class Address:
    depedencies = ["language"]

    def generate(properties):
        if properties['language']['language'] == 'english':
            return {'prop_title': 'Address', 'address': 'Not available in English yet!'}
        region = choice(load(open('langs/' + properties['language']['language'] + '/cities.json')))

        country_state = region['region_name']
        city = choice(region['cities'])

        try:
            city_street = choice(city['streets'])
        except (IndexError, KeyError):
            city_street = city['name']

        return {
            'prop_title': 'Address',
            'country_code': properties['language']['country_code'],
            'country_state': country_state,
            'country_city': city['name'],
            'city_postcode': city['postcode'],
            'city_street': city_street,
            'city_latitude': city['lat'],
            'city_longitude': city['lon'],
            'street_number': randint(1, 1000)
        }
