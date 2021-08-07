from random import randint
from datetime import datetime

class Ssn:
    dependencies = ['birthdate', 'language']

    def generate(properties):
        if properties['language']['language'] == 'english_us':
            return {
                'prop_title': 'SSN',
                'ssn': 'Not available in US yet!'
            }
        elif properties['language']['language'] == 'polish':
            gender = properties['gender']['gender']

            date = list(map(int, str(int(datetime(
                properties['birthdate']['birth_year'],
                properties['birthdate']['birth_month'],
                properties['birthdate']['birth_day']
            ).strftime('%Y%m%d')))))

            date[4] += 2 if int(date[0]) == 2 else 0

            pesel = date[2:]

            while len(pesel) < 10:
                pesel.append(randint(0, 9))

            pesel[9] = 0 if gender == 'female' else 1

            # checksum
            pesel.append((
                9 * pesel[0] +
                7 * pesel[1] +
                3 * pesel[2] +
                pesel[3] +
                9 * pesel[4] +
                7 * pesel[5] +
                3 * pesel[6] +
                pesel[7] +
                9 * pesel[8] +
                7 * pesel[9]
            ) % 10)

            return {
                'prop_title': 'SSN',
                'pesel': ''.join(map(str, pesel))
            }
