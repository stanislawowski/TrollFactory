"""Blood type generation prop for TrollFactory."""

from typing import List
from random import choices


class BloodType:
    """Blood type generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Blood type generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies: List[str] = []

    def generate(self) -> dict:
        """Generate the blood type."""
        blood_types = ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']
        blood_weights = [35, 13, 30, 8, 8, 2, 2, 1]

        return {
            'prop_title': 'Blood type',
            'blood_type': choices(blood_types, weights=blood_weights)[0],
        }
