"""Phone data generation prop for TrollFactory."""

from random import choice, randint
from pkgutil import get_data
from typing import Optional, TypedDict
from json import loads
from uuid import uuid4


class PhoneType(TypedDict):
    """Type hint for the phone data property."""

    prop_title: str
    phone_brand: str
    phone_model: str
    phone_operator: Optional[str]
    phone_number: Optional[str]
    phone_operating_system: str
    receive_sms: str
    send_sms: str
    phone_call: str
    phone_uuid: str


def generate_phone(language: str) -> dict:
    """Generate a dict with phone data."""
    return choice(loads(get_data(__package__,
                                 'langs/'+language+'/phones.json')))


def generate_phone_brand(phone: dict) -> str:
    """Generate a phone brand."""
    return phone['brand']


def generate_phone_model(phone: dict) -> str:
    """Generate a phone model."""
    return phone['model']


def generate_phone_operator(language: str) -> Optional[str]:
    """Generate a phone operator."""
    if language == 'polish':
        return choice(list(loads(get_data(
            __package__, 'langs/polish/phone-prefixes.json')).items()))[0]
    if language == 'english_us':
        return choice(['AT&T', 'T-Mobile', 'Verizon', 'Mint Mobile'])
    return None


def generate_phone_number(language: str,
                          phone_operator: Optional[str]) -> Optional[str]:
    """Generate a phone number."""
    if language == 'polish':
        prefix = choice([i for i in list(loads(get_data(
            __package__, 'langs/polish/phone-prefixes.json')).items()
            ) if i[0] == phone_operator][0][1])
        return '+48'+prefix+''.join([str(randint(0, 9)) for _ in range(6)])

    if language == 'english_us':
        return ('+1' + str(randint(2, 9))
                + ''.join([str(randint(0, 9)) for _ in range(2)])
                + str(randint(2, 9))
                + ''.join([str(randint(0, 9)) for _ in range(6)]))

    return None


def generate_phone_operating_system(phone: dict) -> str:
    """Generate a phone operating system."""
    return phone['os']


def generate_phone_uuid() -> str:
    """Generate a phone UUID."""
    return str(uuid4())


def generate_receive_sms_url() -> str:
    """Generate a SMS receiving service URL."""
    return 'https://freephonenum.com/receive-sms/random'


def generate_send_sms_url() -> str:
    """Generate a SMS sending service URL."""
    return 'https://sms.priv.pl/'


def generate_phone_call_url() -> str:
    """Generate a phone call service URL."""
    return 'https://freephonenum.com/phone-call'


class Phone:
    """Phone data generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = ['address'] if 'address' \
            not in properties else []

    def generate(self) -> PhoneType:
        """Generate the phone data."""
        # Used properties
        language: str = self.properties['language']['language']

        # Generate data
        phone: dict = generate_phone(language)
        phone_brand: str = generate_phone_brand(phone)
        phone_model: str = generate_phone_model(phone)
        phone_operator: Optional[str] = generate_phone_operator(language)
        phone_number: Optional[str] = generate_phone_number(language,
                                                            phone_operator)
        phone_operating_system: str = generate_phone_operating_system(phone)
        phone_uuid: str = generate_phone_uuid()
        receive_sms_url: str = generate_receive_sms_url()
        send_sms_url: str = generate_send_sms_url()
        phone_call_url: str = generate_phone_call_url()

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
