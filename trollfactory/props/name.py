"""Name generation prop for TrollFactory."""

from typing import TypedDict, Callable


class NameType(TypedDict):
    """Type hint for a name property."""

    prop_title: str
    name: str
    surname: str


class Name:
    """Name generation prop for TrollFactory."""

    def __init__(self, properties: dict, generator: Callable) -> None:
        self.properties = properties
        self.generator: Callable = generator
        self.unresolved_dependencies: tuple = ()

    def generate(self) -> NameType:
        """Generate the name."""
        return NameType({
            'prop_title': 'Name',
            'name': self.generator('name', self.properties),
            'surname': self.generator('surname', self.properties),
        })
