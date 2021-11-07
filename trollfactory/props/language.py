"""Language generation prop for TrollFactory."""

from typing import TypedDict


class LanguageType(TypedDict):
    """Type hint for a language."""

    prop_title: str
    language: str


class Language:
    """Language generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

    def generate(self) -> LanguageType:
        """Generate the language."""
        # Used properties
        language: str = self.properties['language']['language']

        return {
            'prop_title': 'Language',
            'language': language,
        }
