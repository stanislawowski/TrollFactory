"""ID document data generation prop for TrollFactory."""

from typing import List, Any
from random import randint
from datetime import date


class DocumentId:
    """ID document data generation prop class."""

    def __init__(self, properties: dict) -> None:
        """ID document data generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies = ['language'] if 'language' not in \
            properties else []

    def generate(self) -> dict:
        """Generate the ID document data."""
        language = self.properties['language']['language']

        if language == 'english_us':
            return {'prop_title': 'Document - ID', 'document_id': 'N/A'}

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

            today = date.today()
            expiry_date = today + (date(today.year + randint(1, 9), 1, 1)
                                   - date(today.year, 1, 1))

        return {
            'prop_title': 'Document - ID',
            'id_number': ''.join(map(str, id_number)),
            'expiry_date': expiry_date.strftime("%d/%m/%Y"),
        }
