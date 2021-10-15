class Gender:
    def generate(properties: dict) -> dict:
        return {
            'prop_title': 'Gender',
            'gender': properties['gender']['gender'],
        }
