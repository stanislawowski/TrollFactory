from calendar import monthrange
from random import choice, randint
from datetime import datetime, date

class Birthdate:
    def generate(properties):
        current_year = datetime.now().year

        birth_year = randint(current_year-80, current_year)
        birth_month = randint(1,12)
        birth_day = choice(monthrange(birth_year, birth_month))
        if birth_day == 0: birth_day = 1

        today = date.today()

        zodiac_signs = [
            {'name': 'Aries', 'day_s': 18, 'month_s': 4, 'day_e': 13, 'month_e': 5},
            {'name': 'Taurus', 'day_s': 13, 'month_s': 5, 'day_e': 21, 'month_e': 6},
            {'name': 'Gemini', 'day_s': 21, 'month_s': 6, 'day_e': 20, 'month_e': 7},
            {'name': 'Cancer', 'day_s': 20, 'month_s': 7, 'day_e': 10, 'month_e': 8},
            {'name': 'Leo', 'day_s': 10, 'month_s': 8, 'day_e': 16, 'month_e': 9},
            {'name': 'Virgo', 'day_s': 16, 'month_s': 9, 'day_e': 30, 'month_e': 10},
            {'name': 'Libra', 'day_s': 30, 'month_s': 10, 'day_e': 23, 'month_e': 11},
            {'name': 'Scorpio', 'day_s': 23, 'month_s': 11, 'day_e': 29, 'month_e': 11},
            {'name': 'Sagittarius', 'day_s': 17, 'month_s': 12, 'day_e': 20, 'month_e': 1},
            {'name': 'Capricorn', 'day_s': 20, 'month_s': 1, 'day_e': 16, 'month_e': 2},
            {'name': 'Aquarius', 'day_s': 16, 'month_s': 2, 'day_e': 11, 'month_e': 3},
            {'name': 'Pisces', 'day_s': 11, 'month_s': 3, 'day_e': 18, 'month_e': 4}
        ]

        for sign in zodiac_signs:
            if birth_month == sign['month_s'] and birth_day > sign['day_s']:
                zodiac = sign['name']
                break
            elif birth_month == sign['month_e'] and birth_day < sign['day_e']:
                zodiac = sign['name']
                break
            else:
                zodiac = 'Unknown'

        return {
            'prop_title': 'Birthdate',
            'birth_year': birth_year,
            'birth_month': birth_month,
            'birth_day': birth_day,
            'age': today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day)),
            'zodiac': zodiac
        }
