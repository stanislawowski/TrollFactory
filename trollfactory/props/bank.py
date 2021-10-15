"""Bank account data generation prop for TrollFactory."""

from random import randint
from schwifty import IBAN


class Bank:
    """Bank account data generation prop class."""

    dependencies = ['birthdate', 'language']

    def generate_iban(bank_code: str) -> str:
        """Generate the IBAN number."""
        return IBAN.generate(
            'PL',
            bank_code=bank_code,
            account_code='0000' + str(randint(11111111, 99999999)) + '0000',
        ).formatted

    def generate(properties: dict) -> dict:
        """Generate the bank account data."""
        if properties['language']['language'] == 'english_us':
            return {
                'prop_title': 'Bank',
                'bank': 'Not available in US yet!',
            }

        if properties['birthdate']['age'] < 13:
            return {
                'prop_title': 'Bank',
                'iban': None,
            }

        return {
            'prop_title': 'Bank',
            'iban_pekao': Bank.generate_iban('12400001'),
            'iban_mbank': Bank.generate_iban('11402004'),
            'iban_ing': Bank.generate_iban('10501012'),
            'iban_pko': Bank.generate_iban('10205561'),
        }
