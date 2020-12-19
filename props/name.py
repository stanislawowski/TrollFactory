from json import load
from random import choice

class Name:
    def generate(properties):
        names = load(open('langs/' + properties['language']['language'] + '/names.json'))
        surname = choice(load(open('langs/' + properties['language']['language'] + '/surnames.json')))

        if properties['sex']['sex'] == 'male':
            if surname[-1] == 'a':
                surname = surname[:-1] + 'i'
        elif surname[-1] == 'i': surname = surname[:-1] + 'a'

        return {
            'prop_title': 'Name',
            'name': choice(names[properties['sex']['sex']]),
            'surname': surname,
        }
