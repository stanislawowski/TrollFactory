class Language:
    def generate(properties: dict) -> dict:
        return {
            'prop_title': 'Language',
            'language': properties['language']['language'],
        }
