"""Blood type generation prop for TrollFactory."""

from random import choices


def generate_blood_type() -> str:
    return choices(['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-'],
                   weights=[35, 13, 30, 8, 8, 2, 2, 1])[0]


class BloodType:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

    def generate(self) -> dict[str, str]:
        # Generate data
        blood_type: str = generate_blood_type()

        return {
            'prop_title': 'Blood type',
            'blood_type': blood_type,
        }
