"""Credit card data generation prop for TrollFactory."""

from typing import Optional, TypedDict
from random import randint, choice


CARD_TYPES: dict[str, tuple[tuple[str], int]] = {
    'americanexpress': (('34', '37'), 15),
    'diners': (('300', '301', '302', '303', '304', '305', '36', '38', '39'),
               14),
    'discover': (('6011', '622', '64', '65'), 16),
    'jcb': (('3088', '3096', '3112', '3158', '3337', '35'), 16),
    'mastercard': (('5', '2'), 16),
    'visa': (('4',), 16),
}


class CcType(TypedDict):
    """Type hint for the credit card data property."""

    prop_title: str
    americanexpress: int
    diners: int
    discover: int
    jcb: int
    mastercard: int
    visa: int
    cvv3: int
    cvv4: int
    expiry_date: str


def generate_card_number(card_type: str) -> int:
    """Generate a CC number."""
    number = choice(CARD_TYPES[card_type][0])
    number += ''.join([str(randint(1, 9)) for _ in range(
        CARD_TYPES[card_type][1] - len(number) - 1)])

    digits = list(map(int, number + '0'))
    luhn = (
        sum(digits[-1::-2])
        + sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    ) % 10

    return int(number + str((10 - luhn) % 10))


def generate_cvv3() -> int:
    """Generate a 3-digit CVV number."""
    return randint(100, 999)


def generate_cvv4() -> int:
    """Generate a 4-digit CVV number."""
    return randint(1000, 9999)


def generate_expiry_date() -> str:
    """Generate a CC expiry date."""
    return str(randint(1, 12)).zfill(2) + '/' + str(randint(25, 33))


class Cc:
    """Credit card data generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: tuple[str] = ('birthdate',) if \
            'birthdate' not in properties else ()

    def generate(self) -> Optional[CcType]:
        """Generate the credit card data."""
        # Used properties
        age: int = self.properties['birthdate']['age']

        if age < 18:
            return None

        # Generate data
        americanexpress: int = generate_card_number('americanexpress')
        diners: int = generate_card_number('diners')
        discover: int = generate_card_number('discover')
        jcb: int = generate_card_number('jcb')
        mastercard: int = generate_card_number('mastercard')
        visa: int = generate_card_number('visa')
        cvv3: int = generate_cvv3()
        cvv4: int = generate_cvv4()
        expiry_date: str = generate_expiry_date()

        return {
            'prop_title': 'CC',
            'americanexpress': americanexpress,
            'diners': diners,
            'discover': discover,
            'jcb': jcb,
            'mastercard': mastercard,
            'visa': visa,
            'cvv3': cvv3,
            'cvv4': cvv4,
            'expiry_date': expiry_date,
        }
