from random import randint
from schwifty import IBAN

class Iban:
    dependencies = ['birthdate', 'language']
    def generate(properties):
        if properties['language']['language'] == 'english':
            return {'prop_title': 'IBAN', 'iban': 'Not available in English yet!'}
        if properties['birthdate']['age'] < 13:
            return {'prop_title': 'IBAN', 'iban': None}
        return {
            'prop_title': 'IBAN',
            'pekao': IBAN.generate('PL', bank_code='12400001', account_code='0000'+str(randint(11111111, 99999999))+'0000').formatted,
            'mbank': IBAN.generate('PL', bank_code='11402004', account_code='0000'+str(randint(11111111, 99999999))+'0000').formatted,
            'ing': IBAN.generate('PL', bank_code='10501012', account_code='0000'+str(randint(11111111, 99999999))+'0000').formatted,
            'pko': IBAN.generate('PL', bank_code='10205561', account_code='0000'+str(randint(11111111, 99999999))+'0000').formatted,
        }
