from json import loads
from random import choice, choices
from pkgutil import get_data


class Name:
    def generate(properties):
        names = loads(get_data(
            __package__,
            'langs/' + properties['language']['language'] + '/names.json',
        ))[properties['gender']['gender']]

        surname = choice(loads(get_data(
            __package__,
            'langs/' + properties['language']['language'] + '/surnames.json',
        )))

        if properties['language']['language'] == 'polish':
            if properties['gender']['gender'] == 'male':
                if surname[-1] == 'a':
                    surname = surname[:-1] + 'i'
            elif surname[-1] == 'i':
                surname = surname[:-1] + 'a'

        name = choices(
            [i[0] for i in names],
            weights=[i[1] for i in names],
        )[0]

        return {
            'prop_title': 'Name',
            'name': name,
            'surname': surname,
        }
