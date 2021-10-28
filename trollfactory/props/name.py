"""Name generation prop for TrollFactory."""

from typing import Any
from json import loads
from random import choice, choices
from pkgutil import get_data


def generate_name(language: str, gender: str) -> str:
    names: list[list[Any]] = loads(get_data(__package__,
                                            'langs/'+language+'/names.json')
                                   )[gender]
    return choices([i[0] for i in names], weights=[i[1] for i in names])[0]


def generate_surname(language: str, gender: str) -> str:
    surname: str = choice(loads(get_data(__package__,
                                         'langs/'+language+'/surnames.json')))

    if language == 'polish':
        if gender == 'male':
            if surname[-1] == 'a':
                surname = surname[:-1] + 'i'
        elif surname[-1] == 'i':
            surname = surname[:-1] + 'a'

    return surname


class Name:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

    def generate(self) -> dict[str, str]:
        # Used properties
        language: str = self.properties['language']['language']
        gender: str = self.properties['gender']['gender']

        # Generate data
        name: str = generate_name(language, gender)
        surname: str = generate_surname(language, gender)

        return {
            'prop_title': 'Name',
            'name': name,
            'surname': surname,
        }
