"""Social Security number generation prop for TrollFactory."""

from random import randint
from typing import Optional
from datetime import datetime


def generate_ssn(language: str, gender: str, birth_year: int, birth_month: int,
                 birth_day: int) -> Optional[str]:
    if language == 'polish':
        date = list(map(int, str(int(datetime(
            birth_year, birth_month, birth_day).strftime('%Y%m%d')))))

        date[4] += 2 if int(date[0]) == 2 else 0

        pesel = date[2:]

        while len(pesel) < 10:
            pesel.append(randint(0, 9))

        pesel[9] = 0 if gender == 'female' else 1

        # checksum
        pesel.append((9 * pesel[0] + 7 * pesel[1] + 3 * pesel[2] + pesel[3]
                      + 9 * pesel[4] + 7 * pesel[5] + 3 * pesel[6] + pesel[7]
                      + 9 * pesel[8] + 7 * pesel[9]) % 10)
        return ''.join(map(str, pesel))

    return None


class Ssn:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies = []

        for dependency in ['birthdate', 'language']:
            if dependency not in self.properties:
                self.unresolved_dependencies.append(dependency)

    def generate(self) -> Optional[dict]:
        # Used properties
        language = self.properties['language']['language']
        gender = self.properties['gender']['gender']
        birth_year = self.properties['birthdate']['birth_year']
        birth_month = self.properties['birthdate']['birth_month']
        birth_day = self.properties['birthdate']['birth_day']

        # TODO: finish the english_us dataset and remove this
        if language == 'english_us':
            return None

        # Generate data
        ssn = generate_ssn(language, gender, birth_year, birth_month,
                           birth_day)

        return {
            'prop_title': 'SSN',
            'ssn': ssn,
        }
