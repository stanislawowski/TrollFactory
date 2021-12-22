"""Birthdate generation prop for TrollFactory."""

from typing import TypedDict, Callable
from calendar import monthrange
from datetime import date
from random import randint

now = date.today()


class BirthdateType(TypedDict):
    """Type hint for the birthdate property."""

    prop_title: str
    birth_year: int
    birth_month: int
    birth_day: int
    age: int


def generate_age(static: dict) -> int:
    """Generate an age."""
    if 'birthdate' in static and 'age' in static['birthdate']:
        age = static['birthdate']['age']

        # https://en.wikipedia.org/wiki/List_of_the_verified_oldest_people
        assert int(age) in range(1, 123), 'Invalid age!'
    else:
        age = randint(1, 122)

    return age


def generate_birth_year(age: int, static: dict) -> int:
    """Generate a birth year."""
    if 'birthdate' in static and 'birth_year' in static['birthdate']:
        birth_year = int(static['birthdate']['birth_year'])
        assert birth_year in (now.year-age, now.year-age-1), 'Invalid year!'
    else:
        birth_year = now.year - age

    return birth_year


def generate_birth_month(age: int, year: int, static: dict) -> int:
    """Generate a birth month."""
    if 'birthdate' in static and 'birth_month' in static['birthdate']:
        birth_month = int(static['birthdate']['birth_month'])
        assert birth_month in range(1, 13), 'Invalid month!'

        if year == now.year-age-1:
            assert birth_month not in range(1, now.month), 'Invalid month!'
    else:
        if year == now.year-age-1:
            birth_month = randint(now.month, 12)
        else:
            birth_month = randint(1, 12)

    return birth_month


def generate_birth_day(age: int, year: int, month: int, static: dict) -> int:
    """Generate a birth day."""
    if 'birthdate' in static and 'birth_day' in static['birthdate']:
        birth_day = int(static['birthdate']['birth_day'])
        assert birth_day in range(1, monthrange(year, month)[1]+1), \
            'Invalid day!'

        if year == now.year-age-1 and month == now.month:
            assert birth_day > now.day, 'Invalid day!'
    else:
        if year == now.year-age-1 and month == now.month:
            birth_day = randint(now.day+1, monthrange(year, month)[1])
        else:
            birth_day = randint(1, monthrange(year, month)[1])
            if birth_day == 0:
                birth_day = 1

    return birth_day

class Birthdate:
    """Birthdate generation prop for TrollFactory."""

    def __init__(self, properties: dict, generator: Callable) -> None:
        self.properties = properties
        self.generator = generator
        self.unresolved_dependencies: tuple = ()

    def generate(self) -> BirthdateType:
        """Generate the birthdate."""
        data: dict = {
            'prop_title': 'Birthdate',
            'age': generate_age(self.properties),
        }

        data['birth_year'] = generate_birth_year(data['age'], self.properties)
        data['birth_month'] = generate_birth_month(
            data['age'], data['birth_year'], self.properties)
        data['birth_day'] = generate_birth_day(
            data['age'], data['birth_year'], data['birth_month'],
            self.properties)

        return data
