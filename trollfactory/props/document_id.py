"""ID document data generation prop for TrollFactory."""

from typing import List, Any, Optional
from random import randint
from datetime import date


def generate_id_number(language: str) -> Optional[str]:
    if language == 'polish':
        id_number: List[Any] = []

        while len(id_number) < 3:
            id_number.append(chr(randint(65, 90)))
        while len(id_number) < 9:
            id_number.append(randint(0, 9))

        checksum = ((ord(id_number[0]) - 55) * 7
                    + (ord(id_number[1]) - 55) * 3
                    + (ord(id_number[2]) - 55)
                    + id_number[4] * 7
                    + id_number[5] * 3
                    + id_number[6]
                    + id_number[7] * 7
                    + id_number[8] * 3)

        id_number[3] = checksum % 10

        checksum = ((ord(id_number[0]) - 55) * 7
                    + (ord(id_number[1]) - 55) * 3
                    + (ord(id_number[2]) - 55)
                    + id_number[3] * 9
                    + id_number[4] * 7
                    + id_number[5] * 3
                    + id_number[6]
                    + id_number[7] * 7
                    + id_number[8] * 3)

        return ''.join(map(str, id_number))

    if language == 'english_us':
        return 'N/A'

    return None


def generate_expiry_date(language: str) -> Optional[str]:
    if language == 'polish':
        today = date.today()
        return (today + (date(today.year + randint(1, 9), 1, 1)
                - date(today.year, 1, 1))).strftime("%d/%m/%Y")

    if language == 'english_us':
        return 'N/A'

    return None


class DocumentId:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies = ['language'] if 'language' not in \
            properties else []

    def generate(self) -> Optional[dict]:
        # Used properties
        language = self.properties['language']['language']

        # Generate data
        id_number = generate_id_number(language)
        expiry_date = generate_expiry_date(language)

        return {
            'prop_title': 'Document - ID',
            'id_number': id_number,
            'expiry_date': expiry_date,
        }
