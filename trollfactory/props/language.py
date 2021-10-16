"""Language generation prop for TrollFactory."""

from typing import List


class Language:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: List[str] = []

    def generate(self) -> dict:
        # Used properties
        language = self.properties['language']['language']

        return {'prop_title': 'Language', 'language': language}
