"""Colors data generation prop for TrollFactory."""

from random import choice

COLORS: dict[str, list[str]] = {
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
        self.unresolved_dependencies: list[str] = []

    def generate(self) -> dict[str, str]:
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
