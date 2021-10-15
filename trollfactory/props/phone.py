from uuid import uuid4
from json import loads
from random import choice, randint
from pkgutil import get_data


class Phone:
    depedencies = ['address']

    def generate(properties: dict) -> dict:
        data = loads(get_data(
            __package__,
            'langs/' + properties['language']['language'] + '/phones.json',
        ))
        phone = choice(data)

        if properties['language']['language'] == 'polish':
            prefixes = loads(get_data(
                __package__,
                'langs/polish/phone-prefixes.json',
            ))

            phone_operator, phone_prefixes = choice(list(prefixes.items()))
            phone_number = (
                '+48' +
                choice(phone_prefixes) +
                "".join([str(randint(0, 9)) for i in range(6)])
            )
        elif properties['language']['language'] == 'english_us':
            phone_operator = choice([
                'AT&T', 'T-Mobile', 'Verizon', 'Mint Mobile',
            ])
            phone_number = 'Not available in US yet!'

        return {
            'prop_title': 'Phone',
            'brand': phone['brand'],
            'model': phone['model'],
            'operator': phone_operator,
            'number': phone_number,
            'receive_sms': 'https://freephonenum.com/receive-sms/random',
            'send_sms': 'https://sms.priv.pl/',
            'phone_call': 'https://freephonenum.com/phone-call',
            'os': phone['os'],
            'uuid': str(uuid4()),
        }
