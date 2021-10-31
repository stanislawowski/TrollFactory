"""Gender generation prop for TrollFactory."""


class Gender:
    """Gender generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

    def generate(self) -> dict[str, str]:
        """Generate the gender."""
        # Used properties
        gender: str = self.properties['gender']['gender']

        return {'prop_title': 'Gender', 'gender': gender}
