from json import loads
from random import choice, choices
from pkgutil import get_data

class Name:
    def generate(properties):
        names_file = loads(get_data(
            __package__,
            'langs/' + properties['language']['language'] + '/names.json'
        ))
        surname = choice(loads(get_data(
            __package__,
            'langs/' + properties['language']['language'] + '/surnames.json'
        )))

        if properties['gender']['gender'] == 'male':
            if surname[-1] == 'a':
                surname = surname[:-1] + 'i'
        elif surname[-1] == 'i': surname = surname[:-1] + 'a'

        names = [i[0] for i in names_file[properties['gender']['gender']]]
        names_weights = [i[1] for i in names_file[properties['gender']['gender']]]

        name = choices(names, weights=names_weights)[0]

        return {
            'prop_title': 'Name',
            'name': name,
            'surname': surname,
        }
