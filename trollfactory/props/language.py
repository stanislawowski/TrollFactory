"""Language generation prop for TrollFactory."""


class Language:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

    def generate(self) -> dict[str, str]:
        # Used properties
        language: str = self.properties['language']['language']

        return {'prop_title': 'Language', 'language': language}
