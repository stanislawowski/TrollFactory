"""Language generation prop for TrollFactory."""

from typing import TypedDict, Callable


class LanguageType(TypedDict):
    """Type hint for a language."""

    prop_title: str
    language: str
    dataset: str


class Language:
    """Language generation prop for TrollFactory."""

    def __init__(self, properties: dict, generator: Callable) -> None:
        self.properties = properties
        self.generator = generator
        self.unresolved_dependencies: tuple = ()

    def generate(self) -> LanguageType:
        """Generate the language."""
        return {
            'prop_title': 'Language',
            'language': self.generator('language', self.properties),
            'dataset': self.properties['language']['dataset'],
        }
