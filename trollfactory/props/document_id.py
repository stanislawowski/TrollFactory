"""ID document data generation prop for TrollFactory."""

from typing import Any, Optional, TypedDict
from random import randint
from datetime import date


class DocumentIdType(TypedDict):
    """Type hint for the ID document data property."""

    prop_title: str
    id_number: Optional[str]
    expiry_date: Optional[str]


def generate_id_number(language: str) -> Optional[str]:
    """Generate an ID document number."""
    if language == 'polish':
        id_number: list[Any] = []

        while len(id_number) < 3:
            id_number.append(chr(randint(65, 90)))
        while len(id_number) < 9:
            id_number.append(randint(0, 9))

        checksum: int = ((ord(id_number[0]) - 55) * 7
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

    return None


def generate_expiry_date(language: str) -> Optional[str]:
    """Generate an ID document expiry date."""
    if language == 'polish':
        today: date = date.today()
        return (today + (date(today.year + randint(1, 9), 1, 1)
                - date(today.year, 1, 1))).strftime("%d/%m/%Y")

    return None


class DocumentId:
    """ID document data generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: tuple[str] = ('language',) if \
            'language' not in properties else ()

    def generate(self) -> Optional[DocumentIdType]:
        """Generate the ID document data."""
        # Used properties
        language: str = self.properties['language']['language']

        # N/A for US
        if language == 'english_us':
            return None

        # Generate data
        id_number: Optional[str] = generate_id_number(language)
        expiry_date: Optional[str] = generate_expiry_date(language)

        return {
            'prop_title': 'Document - ID',
            'id_number': id_number,
            'expiry_date': expiry_date,
        }
