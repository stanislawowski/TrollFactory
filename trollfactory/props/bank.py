"""Bank account data generation prop for TrollFactory."""

from typing import Optional
from random import randint
from schwifty import IBAN


def generate_iban(bank_code: str) -> str:
    return IBAN.generate(
        'PL', bank_code=bank_code,
        account_code='0000' + str(randint(11111111, 99999999)) + '0000',
    ).formatted


class Bank:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

        for dependency in ['birthdate', 'language']:
            if dependency not in self.properties:
                self.unresolved_dependencies.append(dependency)

    def generate(self) -> Optional[dict[str, str]]:
        # Used properties
        language: str = self.properties['language']['language']
        age: int = self.properties['birthdate']['age']

        # TODO: finish the english_us dataset and remove this
        if language == 'english_us':
            return None

        # TODO: find legal basis for this for all the datasets
        if age < 13:
            return None

        # Generate data
        iban_pekao: str = generate_iban('12400001')
        iban_mbank: str = generate_iban('11402004')
        iban_ing: str = generate_iban('10501012')
        iban_pko: str = generate_iban('10205561')

        return {
            'prop_title': 'Bank',
            'iban_pekao': iban_pekao,
            'iban_mbank': iban_mbank,
            'iban_ing': iban_ing,
            'iban_pko': iban_pko,
        }
