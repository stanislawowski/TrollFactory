"""Credit card data generation prop for TrollFactory."""

from typing import Optional, TypedDict
from random import randint


class CcType(TypedDict):
    """Type hint for the credit card data property."""

    prop_title: str
    mastercard: str
    visa: str
    americanexpress: str
    cvv: int
    expiry_date: str


def generate_card_number(card_type: str) -> str:
    """Generate a CC number."""
    if card_type == 'mastercard':
        initial, rem = [5, randint(1, 5)], 16 - 2
    elif card_type == 'visa':
        initial, rem = [4], 16 - 1
    elif card_type == 'americanexpress':
        initial, rem = [3, randint(4, 7)], 13

    nums: list[int] = initial + [randint(1, 9) for _ in range(rem - 1)]

    check_sum: int = 0
    check_offset: int = (len(nums) + 1) % 2

    for i, n in enumerate(nums):
        if (i + check_offset) % 2 == 0:
            n_: int = n * 2
            check_sum += n_ - 9 if n_ > 9 else n_
        else:
            check_sum += n
    final: list[int] = nums + [10 - (check_sum % 10)]

    return ''.join(map(str, final))


def generate_cvv() -> int:
    """Generate a CVV number."""
    return randint(100, 999)


def generate_expiry_date() -> str:
    """Generate a CC expiry date."""
    return str(randint(1, 12)).zfill(2) + '/' + str(randint(25, 33))


class Cc:
    """Credit card data generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = ['birthdate'] if 'birthdate'\
            not in properties else []

    def generate(self) -> Optional[CcType]:
        """Generate the credit card data."""
        # Used properties
        age: int = self.properties['birthdate']['age']

        if age < 18:
            return None

        # Generate data
        mastercard: str = generate_card_number('mastercard')
        visa: str = generate_card_number('visa')
        americanexpress: str = generate_card_number('americanexpress')
        cvv: int = generate_cvv()
        expiry_date: str = generate_expiry_date()

        return {
            'prop_title': 'CC',
            'mastercard': mastercard,
            'visa': visa,
            'americanexpress': americanexpress,
            'cvv': cvv,
            'expiry_date': expiry_date,
        }
