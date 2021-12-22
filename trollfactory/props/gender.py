"""Gender generation prop for TrollFactory."""

from typing import TypedDict, Callable
from random import choice


class GenderType(TypedDict):
    """Type hint for a gender property."""

    prop_title: str
    gender: str


class Gender:
    """Gender generation prop for TrollFactory."""

    def __init__(self, properties: dict, generator: Callable) -> None:
        self.properties = properties
        self.generator = generator
        self.unresolved_dependencies: tuple = ()

    def generate(self) -> GenderType:
        """Generate the gender."""
        return {
            'prop_title': 'Gender',
            'gender': self.generator('gender', self.properties),
        }
