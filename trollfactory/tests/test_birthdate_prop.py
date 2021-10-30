from datetime import date
from trollfactory.props import birthdate as prop


def test_generated_birth_year():
    year = prop.generate_birth_year()
    assert isinstance(year, int) and len(str(year)) == 4


def test_generated_birth_month():
    month = prop.generate_birth_month()
    assert isinstance(month, int) and month in range(1, 13)


def test_generated_birth_day():
    day = prop.generate_birth_day(2021, 10)
    assert isinstance(day, int) and day in range(1, 32)


def test_generated_age():
    age = prop.generate_age(2021, 10, 10)
    today = date.today()
    assert age == (today.year - 2021 - ((today.month, today.day) < (10, 10)))


def test_generated_zodiac():
    assert prop.generate_zodiac(5, 18) == 'Taurus'


def test_generated_prop():
    assert prop.Birthdate({}).generate()
