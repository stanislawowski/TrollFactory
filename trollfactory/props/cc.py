"""Credit card data generation prop for TrollFactory."""

from random import randint


def generate_card(card_type):
    """Generate the credit card mumber."""
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

    return "".join(map(str, final))


class Cc:
    """Credit card data generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Credit card data generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies = ['birthdate'] if 'birthdate' not in \
            properties else []

    def generate(self) -> dict:
        """Generate the credit card data."""
        age = self.properties['birthdate']['age']

        if age < 13:
            return {'prop_title': 'CC', 'cc': None}

        return {
            'prop_title': 'CC',
            'mastercard': generate_card('mastercard'),
            'visa': generate_card('visa'),
            'americanexpress': generate_card('americanexpress'),
            'cvv': randint(100, 999),
            'date': str(randint(1, 12)).zfill(2) + '/' + str(randint(25, 33)),
        }
