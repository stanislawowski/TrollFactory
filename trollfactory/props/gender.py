"""Gender generation prop for TrollFactory."""

class Gender:
    """Gender generation prop class."""

    def generate(properties: dict) -> dict:
        """Generate the gender."""
        return {
            'prop_title': 'Gender',
            'gender': properties['gender']['gender'],
        }
