"""Bank account data generation prop for TrollFactory."""

from random import randint
from schwifty import IBAN


def generate_iban(bank_code: str) -> str:
    """Generate the IBAN number."""
    return IBAN.generate(
        'PL', bank_code=bank_code,
        account_code='0000' + str(randint(11111111, 99999999)) + '0000',
    ).formatted


class Bank:
    """Bank account data generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Bank account data generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies = []

        for dependency in ['birthdate', 'language']:
            if dependency not in self.properties:
                self.unresolved_dependencies.append(dependency)

    def generate(self) -> dict:
        """Generate the bank account data."""
        if self.properties['language']['language'] == 'english_us':
            return {
                'prop_title': 'Bank',
                'bank': 'Not available in US yet!',
            }

        if self.properties['birthdate']['age'] < 13:
            return {
                'prop_title': 'Bank',
                'iban': None,
            }

        return {
            'prop_title': 'Bank',
            'iban_pekao': generate_iban('12400001'),
            'iban_mbank': generate_iban('11402004'),
            'iban_ing': generate_iban('10501012'),
            'iban_pko': generate_iban('10205561'),
        }
