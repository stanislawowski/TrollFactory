"""Birthdate generation prop for TrollFactory."""

from typing import TypedDict
from random import choice, randint
from calendar import monthrange
from datetime import date


ZODIAC_SIGNS: tuple[tuple[str, int, int, int]] = (
    ('Aries', 18, 4, 13, 5),
    ('Taurus', 13, 5, 21, 6),
    ('Gemini', 21, 6, 20, 7),
    ('Cancer', 20, 7, 10, 8),
    ('Leo', 10, 8, 16, 9),
    ('Virgo', 16, 9, 30, 10),
    ('Libra', 30, 10, 23, 11),
    ('Scorpio', 23, 11, 29, 11),
    ('Sagittarius', 17, 12, 20, 1),
    ('Capricorn', 20, 1, 16, 2),
    ('Aquarius', 16, 2, 11, 3),
    ('Pisces', 11, 3, 18, 4),
)


class BirthdateType(TypedDict):
    """Type hint for the birthdate property."""

    prop_title: str
    birth_year: int
    birth_month: int
    birth_day: int
    age: int
    zodiac: str


def generate_birth_year() -> int:
    """Generate a birth year."""
    current_year: int = date.today().year
    return randint(current_year-80, current_year)


def generate_birth_month() -> int:
    """Generate a birth month."""
    return randint(1, 12)


def generate_birth_day(birth_year: int, birth_month: int) -> int:
    """Generate a birth day."""
    birth_day: int = choice(monthrange(birth_year, birth_month))
    return birth_day if birth_day != 0 else 1


def generate_age(birth_year: int, birth_month: int, birth_day: int) -> int:
    """Generate an age."""
    today: date = date.today()
    return today.year - birth_year - ((today.month, today.day)
                                      < (birth_month, birth_day))


def generate_zodiac(birth_month: int, birth_day: int) -> str:
    """Generate a zodiac sign."""
    zodiac: str = 'Unknown'
    for sign in ZODIAC_SIGNS:
        if (birth_month == sign[2] and birth_day > sign[1]) or (
                birth_month == sign[4] and birth_day < sign[3]):
            zodiac = sign[0]
            break
    return zodiac


class Birthdate:
    """Birthdate generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: tuple[str] = ()

    def generate(self) -> BirthdateType:
        """Generate the birthdate."""
        # Generate data
        birth_year: int = generate_birth_year()
        birth_month: int = generate_birth_month()
        birth_day: int = generate_birth_day(birth_year, birth_month)
        age: int = generate_age(birth_year, birth_month, birth_day)
        zodiac: str = generate_zodiac(birth_month, birth_day)

        return {
            'prop_title': 'Birthdate',
            'birth_year': birth_year,
            'birth_month': birth_month,
            'birth_day': birth_day,
            'age': age,
            'zodiac': zodiac,
        }
