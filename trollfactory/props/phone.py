"""Phone data generation prop for TrollFactory."""

from random import choice, randint
from pkgutil import get_data
from typing import Optional
from json import loads
from uuid import uuid4


def generate_phone(language: str) -> dict:
    return choice(loads(get_data(__package__,
                                 'langs/'+language+'/phones.json')))


def generate_phone_brand(phone: dict) -> str:
    return phone['brand']


def generate_phone_model(phone: dict) -> str:
    return phone['model']


def generate_phone_operator(language: str) -> Optional[str]:
    if language == 'polish':
        return choice(list(loads(get_data(
            __package__, 'langs/polish/phone-prefixes.json')).items()))[0]
    if language == 'english_us':
        return choice(['AT&T', 'T-Mobile', 'Verizon', 'Mint Mobile'])
    return None


def generate_phone_number(language: str,
                          phone_operator: Optional[str]) -> Optional[str]:
    if language == 'polish':
        prefix = choice([i for i in list(loads(get_data(
            __package__, 'langs/polish/phone-prefixes.json')).items()
            ) if i[0] == phone_operator][0][1])
        return '+48'+prefix+''.join([str(randint(0, 9)) for i in range(6)])
    if language == 'english_us':
        return None  # TODO: finish the english_us dataset and remove this
    return None


def generate_phone_operating_system(phone: dict) -> str:
    return phone['os']


def generate_phone_uuid() -> str:
    return str(uuid4())


def generate_receive_sms_url() -> str:
    return 'https://freephonenum.com/receive-sms/random'


def generate_send_sms_url() -> str:
    return 'https://sms.priv.pl/'


def generate_phone_call_url() -> str:
    return 'https://freephonenum.com/phone-call'


class Phone:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies = ['address'] if 'address' not in \
            properties else []

    def generate(self) -> dict:
        # Used properties
        language = self.properties['language']['language']

        # Generate data
        phone = generate_phone(language)
        phone_brand = generate_phone_brand(phone)
        phone_model = generate_phone_model(phone)
        phone_operator = generate_phone_operator(language)
        phone_number = generate_phone_number(language, phone_operator)
        phone_operating_system = generate_phone_operating_system(phone)
        phone_uuid = generate_phone_uuid()
        receive_sms_url = generate_receive_sms_url()
        send_sms_url = generate_send_sms_url()
        phone_call_url = generate_phone_call_url()

        return {
            'prop_title': 'Phone',
            'phone_brand': phone_brand,
            'phone_model': phone_model,
            'phone_operator': phone_operator,
            'phone_number': phone_number,
            'phone_operating_system': phone_operating_system,
            'receive_sms': receive_sms_url,
            'send_sms': send_sms_url,
            'phone_call': phone_call_url,
            'phone_uuid': phone_uuid,
        }
