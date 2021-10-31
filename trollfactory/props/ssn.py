"""Social Security number generation prop for TrollFactory."""

from random import randint
from typing import Optional
from datetime import datetime


def generate_ssn(language: str, gender: str, birth_year: int, birth_month: int,
                 birth_day: int) -> Optional[str]:
    """Generate a SSN."""
    if language == 'polish':
        date: list[int] = list(map(int, str(int(datetime(
            birth_year, birth_month, birth_day).strftime('%Y%m%d')))))

        date[4] += 2 if int(date[0]) == 2 else 0

        pesel: list[int] = date[2:]

        while len(pesel) < 10:
            pesel.append(randint(0, 9))

        if gender == 'female':
            pesel[9] = 0
        elif gender == 'male':
            pesel[9] = 1
        else:
            # random for non-binary people
            pesel[9] = randint(0, 1)

        # checksum
        pesel.append((9 * pesel[0] + 7 * pesel[1] + 3 * pesel[2] + pesel[3]
                      + 9 * pesel[4] + 7 * pesel[5] + 3 * pesel[6] + pesel[7]
                      + 9 * pesel[8] + 7 * pesel[9]) % 10)
        return ''.join(map(str, pesel))

    return None


class Ssn:
    """Social Security number generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

        for dependency in ['birthdate', 'language']:
            if dependency not in self.properties:
                self.unresolved_dependencies.append(dependency)

    def generate(self) -> Optional[dict[str, Optional[str]]]:
        """Generate the Social Security number."""
        # Used properties
        language: str = self.properties['language']['language']
        gender: str = self.properties['gender']['gender']
        birth_year: int = self.properties['birthdate']['birth_year']
        birth_month: int = self.properties['birthdate']['birth_month']
        birth_day: int = self.properties['birthdate']['birth_day']

        # TODO: finish the english_us dataset and remove this
        if language == 'english_us':
            return None

        # Generate data
        ssn: Optional[str] = generate_ssn(language, gender, birth_year,
                                          birth_month, birth_day)

        return {
            'prop_title': 'SSN',
            'ssn': ssn,
        }
