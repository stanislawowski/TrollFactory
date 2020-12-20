from random import randint
from schwifty import IBAN

class Bank:
    dependencies = ['birthdate', 'language']
    def generate(properties):
        if properties['language']['language'] == 'english':
            return {'prop_title': 'Bank', 'bank': 'Not available in English yet!'}
        if properties['birthdate']['age'] < 13:
            return {'prop_title': 'Bank', 'iban': None}
        return {
            'prop_title': 'Bank',
            'iban_pekao': IBAN.generate('PL', bank_code='12400001', account_code='0000'+str(randint(11111111, 99999999))+'0000').formatted,
            'iban_mbank': IBAN.generate('PL', bank_code='11402004', account_code='0000'+str(randint(11111111, 99999999))+'0000').formatted,
            'iban_ing': IBAN.generate('PL', bank_code='10501012', account_code='0000'+str(randint(11111111, 99999999))+'0000').formatted,
            'iban_pko': IBAN.generate('PL', bank_code='10205561', account_code='0000'+str(randint(11111111, 99999999))+'0000').formatted,
        }
