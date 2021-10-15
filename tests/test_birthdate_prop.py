from datetime import datetime, date
from calendar import monthrange
from trollfactory.props.birthdate import Birthdate

generated_birthdate = Birthdate.generate({})


def test_birthdate_generated():
    assert generated_birthdate['prop_title'] == 'Birthdate'


def test_valid_birth_year():
    current_year = datetime.now().year

    assert generated_birthdate['birth_year'] in range(
            current_year - 80, current_year + 1)


def test_valid_birth_month():
    assert generated_birthdate['birth_month'] in range(1, 13)


def test_valid_birth_day():
    valid_month_range = monthrange(generated_birthdate['birth_year'],
                                   generated_birthdate['birth_month'])
    assert generated_birthdate['birth_day'] in range(valid_month_range[0],
                                                     valid_month_range[1] + 1)


def test_valid_age():
    today = date.today()
    assert today.year - generated_birthdate['birth_year'] - (
        (today.month, today.day) < (generated_birthdate['birth_month'],
                                    generated_birthdate['birth_day']))


def test_zodiac_generated():
    assert isinstance(generated_birthdate['zodiac'], str)
