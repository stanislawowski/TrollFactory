"""Name generation prop for TrollFactory."""

from typing import Any, TypedDict
from json import loads
from random import choice, choices
from pkgutil import get_data


class NameType(TypedDict):
    """Type hint for a name property."""

    prop_title: str
    name: str
    surname: str


def generate_name(language: str, gender: str) -> str:
    """Generate a name."""
    names: list[list[Any]] = loads(get_data(__package__,
                                            'langs/'+language+'/names.json')
                                   )[gender]
    name = choices([i[0] for i in names], weights=[i[1] for i in names])[0]
    return choice(name.split('/'))


def generate_surname(language: str, gender: str) -> str:
    """Generate a surname."""
    surname: str = choice(loads(get_data(__package__,
                                         'langs/'+language+'/surnames.json')))

    if language == 'polish':
        if gender == 'male':
            if surname[-1] == 'a':
                surname = surname[:-1] + 'i'
        elif gender == 'female' and surname[-1] == 'i':
            surname = surname[:-1] + 'a'
        elif gender == 'non-binary':
            if surname[-1] == 'i':
                surname = surname[:-1] + choice(['ie', 'x'])
            elif surname.endswith('ka'):
                surname = surname[:-1] + 'ie'

    return surname


class Name:
    """Name generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

    def generate(self) -> NameType:
        """Generate the name."""
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
