from random import choice, randint
from json import load

class Address:
    depedencies = ["language"]

    def generate(properties):
        region = choice(load(open('langs/' + properties['language']['language'] + '/cities.json')))

        country_state = region['region_name']
        city = choice(region['cities'])
        country_city = city['name']
        city_postcode = city['postcode']

        try:
            city_street = choice(city['streets'])
        except (IndexError, KeyError):
            city_street = city['name']

        return {
            'country_code': properties['language']['country_code'],
            'country_state': country_state,
            'country_city': country_city,
            'city_postcode': city_postcode,
            'city_street': city_street,
            'street_number': randint(1, 1000)
        }
