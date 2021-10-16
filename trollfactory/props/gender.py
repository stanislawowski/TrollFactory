"""Gender generation prop for TrollFactory."""

from typing import List


class Gender:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: List[str] = []

    def generate(self) -> dict:
        # Used properties
        gender = self.properties['gender']['gender']

        return {'prop_title': 'Gender', 'gender': gender}
