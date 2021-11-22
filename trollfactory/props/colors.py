"""Colors data generation prop for TrollFactory."""

from random import choice
from typing import TypedDict

COLORS: dict[str, tuple[str]] = {
    'favourite': ('black', 'white', 'grey', 'red', 'blue', 'navy', 'green',
                  'pink', 'white', 'purple', 'yellow', 'green', 'orange'),
    'hair': ('blonde', 'brown', 'black', 'auburn', 'red'),
    'eyes': ('amber', 'blue', 'brown', 'gray', 'green', 'hazel'),
}


class ColorsType(TypedDict):
    """Type hint for the colors data property."""

    prop_title: str
    favourite_color: str
    hair_color: str
    eyes_color: str


def generate_favourite_color() -> str:
    """Generate a favourite color."""
    return choice(COLORS['favourite'])


def generate_hair_color() -> str:
    """Generate a hair color."""
    return choice(COLORS['hair'])


def generate_eyes_color() -> str:
    """Generate the eyes color."""
    return choice(COLORS['eyes'])


class Colors:
    """Colors data generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: tuple[str] = ()

    def generate(self) -> ColorsType:
        """Generate the colors data."""
        # Generate data
        favourite_color: str = generate_favourite_color()
        hair_color: str = generate_hair_color()
        eyes_color: str = generate_eyes_color()

        return {
            'prop_title': 'Colors',
            'favourite_color': favourite_color,
            'hair_color': hair_color,
            'eyes_color': eyes_color,
        }
