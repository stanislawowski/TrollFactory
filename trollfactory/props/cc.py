"""Credit card data generation prop for TrollFactory."""

from typing import Optional
from random import randint


def generate_card_number(card_type: str) -> str:
    if card_type == 'mastercard':
        initial, rem = [5, randint(1, 5)], 16 - 2
        nums = initial + [randint(1, 9) for x in range(rem - 1)]
    elif card_type == 'visa':
        initial, rem = [4], 16 - 1
        nums = initial + [randint(1, 9) for x in range(rem - 1)]
    elif card_type == 'americanexpress':
        initial, rem = [3, randint(4, 7)], 13
        nums = initial + [randint(1, 9) for x in range(rem - 1)]

    check_sum = 0
    check_offset = (len(nums) + 1) % 2

    for i, n in enumerate(nums):
        if (i + check_offset) % 2 == 0:
            n_ = n * 2
            check_sum += n_ - 9 if n_ > 9 else n_
        else:
            check_sum += n
    final = nums + [10 - (check_sum % 10)]

    return ''.join(map(str, final))


def generate_cvv() -> int:
    return randint(100, 999)


def generate_expiry_date() -> str:
    return str(randint(1, 12)).zfill(2) + '/' + str(randint(25, 33))


class Cc:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies = ['birthdate'] if 'birthdate' not in \
            properties else []

    def generate(self) -> Optional[dict]:
        # Used properties
        age = self.properties['birthdate']['age']

        if age < 18:
            return None

        # Generate data
        mastercard = generate_card_number('mastercard')
        visa = generate_card_number('visa')
        americanexpress = generate_card_number('americanexpress')
        cvv = generate_cvv()
        expiry_date = generate_expiry_date()

        return {
            'prop_title': 'CC',
            'mastercard': mastercard,
            'visa': visa,
            'americanexpress': americanexpress,
            'cvv': cvv,
            'expiry_date': expiry_date,
        }
