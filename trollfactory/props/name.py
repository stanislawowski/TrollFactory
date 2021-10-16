"""Name generation prop for TrollFactory."""

from typing import List
from json import loads
from random import choice, choices
from pkgutil import get_data


class Name:
    """Name generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Name generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies: List[str] = []

    def generate(self) -> dict:
        """Generate the name."""
        language = self.properties['language']['language']
        gender = self.properties['gender']['gender']

        names = loads(get_data(__package__,
                               'langs/'+language+'/names.json'))[gender]

        surname = choice(loads(get_data(__package__,
                                        'langs/'+language+'/surnames.json')))

        if language == 'polish':
            if gender == 'male':
                if surname[-1] == 'a':
                    surname = surname[:-1] + 'i'
            elif surname[-1] == 'i':
                surname = surname[:-1] + 'a'

        name = choices([i[0] for i in names], weights=[i[1] for i in names])[0]

        return {
            'prop_title': 'Name',
            'name': name,
            'surname': surname,
        }
