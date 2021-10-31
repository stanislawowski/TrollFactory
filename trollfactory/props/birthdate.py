"""Birthdate generation prop for TrollFactory."""

from typing import TypedDict, Any
from random import choice, randint
from calendar import monthrange
from datetime import date


class ZodiacSign(TypedDict):
    """Zodiac sign data type hint."""
    name: str
    day_s: int
    month_s: int
    day_e: int
    month_e: int


ZODIAC_SIGNS: list[ZodiacSign] = [
    {'name': 'Aries', 'day_s': 18, 'month_s': 4, 'day_e': 13, 'month_e': 5},
    {'name': 'Taurus', 'day_s': 13, 'month_s': 5, 'day_e': 21, 'month_e': 6},
    {'name': 'Gemini', 'day_s': 21, 'month_s': 6, 'day_e': 20, 'month_e': 7},
    {'name': 'Cancer', 'day_s': 20, 'month_s': 7, 'day_e': 10, 'month_e': 8},
    {'name': 'Leo', 'day_s': 10, 'month_s': 8, 'day_e': 16, 'month_e': 9},
    {'name': 'Virgo', 'day_s': 16, 'month_s': 9, 'day_e': 30, 'month_e': 10},
    {'name': 'Libra', 'day_s': 30, 'month_s': 10, 'day_e': 23, 'month_e': 11},
    {'name': 'Scorpio', 'day_s': 23, 'month_s': 11, 'day_e': 29,
        'month_e': 11},
    {'name': 'Sagittarius', 'day_s': 17, 'month_s': 12, 'day_e': 20,
        'month_e': 1},
    {'name': 'Capricorn', 'day_s': 20, 'month_s': 1, 'day_e': 16,
        'month_e': 2},
    {'name': 'Aquarius', 'day_s': 16, 'month_s': 2, 'day_e': 11, 'month_e': 3},
    {'name': 'Pisces', 'day_s': 11, 'month_s': 3, 'day_e': 18, 'month_e': 4},
]


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
        if (birth_month == sign['month_s'] and birth_day > sign['day_s']) or (
                birth_month == sign['month_e'] and birth_day < sign['day_e']):
            zodiac = sign['name']
            break
    return zodiac


class Birthdate:
    """Birthdate generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

    def generate(self) -> dict[str, Any]:
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
