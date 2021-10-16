"""Colors data generation prop for TrollFactory."""

from typing import List
from random import choice

COLORS = {
    'favourite': ['black', 'white', 'grey', 'red', 'blue', 'navy', 'green',
                  'pink', 'white', 'purple', 'yellow', 'green', 'orange'],
    'hair': ['blonde', 'brown', 'black', 'auburn', 'red'],
    'eyes': ['amber', 'blue', 'brown', 'gray', 'green', 'hazel'],
}


def generate_favourite_color() -> str:
    return choice(COLORS['favourite'])


def generate_hair_color() -> str:
    return choice(COLORS['hair'])


def generate_eyes_color() -> str:
    return choice(COLORS['eyes'])


class Colors:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: List[str] = []

    def generate(self) -> dict:
        # Generate data
        favourite_color = generate_favourite_color()
        hair_color = generate_hair_color()
        eyes_color = generate_eyes_color()

        return {
            'prop_title': 'Colors',
            'favourite_color': favourite_color,
            'hair_color': hair_color,
            'eyes_color': eyes_color,
        }
