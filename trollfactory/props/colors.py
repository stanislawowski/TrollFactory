"""Colors data generation prop for TrollFactory."""

from typing import List
from random import choice

COLORS = {
    'favourite': ['black', 'white', 'grey', 'red', 'blue', 'navy', 'green',
                  'pink', 'white', 'purple', 'yellow', 'green', 'orange'],
    'hair': ['blonde', 'brown', 'black', 'auburn', 'red'],
    'eyes': ['amber', 'blue', 'brown', 'gray', 'green', 'hazel'],
}


class Colors:
    """Colors data generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Colors data generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies: List[str] = []

    def generate(self) -> dict:
        """Generate the colors data."""
        return {
            'prop_title': 'Colors',
            'favourite': choice(COLORS['favourite']),
            'hair': choice(COLORS['hair']),
            'eyes': choice(COLORS['eyes']),
        }
