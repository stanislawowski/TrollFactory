"""Phone data generation prop for TrollFactory."""

from uuid import uuid4
from json import loads
from random import choice, randint
from pkgutil import get_data


class Phone:
    """Phone data generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Phone data generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies = ['address'] if 'address' not in \
            properties else []

    def generate(self) -> dict:
        """Generate the phone data."""
        language = self.properties['language']['language']

        data = loads(get_data(__package__, 'langs/'+language+'/phones.json'))
        phone = choice(data)

        if language == 'polish':
            prefixes = loads(get_data(
                __package__,
                'langs/polish/phone-prefixes.json'))
            phone_operator, phone_prefixes = choice(list(prefixes.items()))
            phone_number = ('+48' + choice(phone_prefixes)
                            + "".join([str(randint(0, 9)) for i in range(6)]))

        elif language == 'english_us':
            phone_operator = choice([
                'AT&T', 'T-Mobile', 'Verizon', 'Mint Mobile'])
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
