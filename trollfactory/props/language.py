"""Language generation prop for TrollFactory."""

class Language:
    """Language generation prop class."""

    def generate(properties: dict) -> dict:
        """Generate the language."""
        return {
            'prop_title': 'Language',
            'language': properties['language']['language'],
        }
