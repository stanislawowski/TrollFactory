from random import randint
from datetime import datetime

class Pesel:
    dependencies = ['birthdate']

    def generate(properties):
        sex = properties['sex']['sex']
        birth_year = properties['birthdate']['birth_year']
        birth_month = properties['birthdate']['birth_month']
        birth_day = properties['birthdate']['birth_day']

        date = datetime(birth_year, birth_month, birth_day)
        date = list(map(int, str(int(date.strftime('%Y%m%d')))))
        if int(date[0]) == 2: date[4] = date[4] + 2
        pesel = date[2:]
        while len(pesel) < 10:
            pesel.append(randint(0, 9))
        if sex == 'female': pesel[9] = 0
        else: pesel[9] = 1
        checksum = (9*pesel[0]+7*pesel[1]+3*pesel[2]+pesel[3]+9*pesel[4]+7*pesel[5]+3*pesel[6]+pesel[7]+9*pesel[8]+7*pesel[9]) % 10
        pesel.append(checksum)

        return {
            'prop_title': 'PESEL',
            'pesel': ''.join(map(str, pesel)),
        }
