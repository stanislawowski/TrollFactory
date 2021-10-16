"""Gender generation prop for TrollFactory."""

from typing import List


class Gender:
    """Gender generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Gender generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies: List[str] = []

    def generate(self) -> dict:
        """Generate the gender."""
        gender = self.properties['gender']['gender']

        return {'prop_title': 'Gender', 'gender': gender}
