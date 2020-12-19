from uuid import uuid4
from json import load
from random import choice

class Phone:
    def generate(properties):
        data = load(open('langs/' + properties['language']['language'] + '/phones.json'))
        phone = choice(data)

        return {
            'prop_title': 'Phone',
            'brand': phone['brand'],
            'model': phone['model'],
            'receive_sms': 'https://freephonenum.com/receive-sms/random',
            'send_sms': 'https://sms.priv.pl/',
            'phone_call': 'https://freephonenum.com/phone-call',
            'os': phone['os'],
            'uuid': str(uuid4())
        }
