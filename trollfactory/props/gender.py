"""Gender generation prop for TrollFactory."""


class Gender:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

    def generate(self) -> dict[str, str]:
        # Used properties
        gender: str = self.properties['gender']['gender']

        return {'prop_title': 'Gender', 'gender': gender}
