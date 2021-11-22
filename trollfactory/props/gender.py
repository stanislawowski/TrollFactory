"""Gender generation prop for TrollFactory."""

from typing import TypedDict


class GenderType(TypedDict):
    """Type hint for a gender property."""

    prop_title: str
    gender: str


class Gender:
    """Gender generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: tuple[str] = ()

    def generate(self) -> GenderType:
        """Generate the gender."""
        # Used properties
        gender: str = self.properties['gender']['gender']

        return {
            'prop_title': 'Gender',
            'gender': gender,
        }
