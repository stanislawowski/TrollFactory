"""Language generation prop for TrollFactory."""

from typing import List


class Language:
    """Language generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Language generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies: List[str] = []

    def generate(self) -> dict:
        """Generate the language."""
        language = self.properties['language']['language']

        return {'prop_title': 'Language', 'language': language}
