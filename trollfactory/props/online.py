"""Online activity data generation prop for TrollFactory."""

from random import choice, randint
from string import ascii_uppercase, ascii_lowercase, digits
from pkgutil import get_data
from json import loads

EMAIL_PROVIDERS = {
    'polish': ['@niepodam.pl'],
    'english_us': ['@armyspy.com', '@cuvox.de', '@dayrep.com', '@einrot.com',
                   '@gustr.com', '@jourrapide.com', '@rhyta.com',
                   '@superrito.com', '@teleworm.us'],
}

EMAIL_URLS = {
    '@niepodam.pl': 'http://niepodam.pl/users/',
    '@armyspy.com': 'http://www.fakemailgenerator.com/#/armyspy.com/',
    '@cuvox.de': 'http://www.fakemailgenerator.com/#/cuvox.de/',
    '@dayrep.com': 'http://www.fakemailgenerator.com/#/dayrep.com/',
    '@einrot.com': 'http://www.fakemailgenerator.com/#/einrot.com/',
    '@gustr.com': 'http://www.fakemailgenerator.com/#/gustr.com/',
    '@jourrapide.com': 'http://www.fakemailgenerator.com/#/jourrapide.com/',
    '@rhyta.com': 'http://www.fakemailgenerator.com/#/rhyta.com/',
    '@superrito.com': 'http://www.fakemailgenerator.com/#/superrito.com/',
    '@teleworm.us': 'http://www.fakemailgenerator.com/#/teleworm.us/',
}

TLDS = ['.pl', '.com', '.com.pl', '.net', '.biz', '.me']


class Online:
    """Online activity data generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Online activity data generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies = []

        for dependency in ['name', 'language']:
            if dependency not in self.properties:
                self.unresolved_dependencies.append(dependency)

    def generate(self) -> dict:
        """Generate the online activity data."""
        name = self.properties['name']['name']
        surname = self.properties['name']['surname']
        language = self.properties['language']['language']

        if ', ' in name:
            name = choice(name.split(', '))

        username = name.lower()[0] + '_' + surname.lower()

        setup = choice(loads(get_data(__package__,
                                      'langs/'+language+'/setups.json')))

        email_provider = choice(EMAIL_PROVIDERS[language])

        password = ''.join(choice(
            ascii_uppercase + ascii_lowercase + digits
        ) for _ in range(16))

        email_url = EMAIL_URLS[email_provider] + username

        ipv6 = ':'.join(
            '{:x}'.format(randint(0, 2**16 - 1)) for i in range(8))

        mac = (
            "02:00:00:%02x:%02x:%02x" % (
                randint(0, 255),
                randint(0, 255),
                randint(0, 255),
            )
        ).upper()

        return {
            'prop_title': 'Online',
            'username': username,
            'email': username + email_provider,
            'receive_email': email_url,
            'domain': username.replace('_', '') + choice(TLDS),
            'password': password,
            'os': setup['os'],
            'browser': setup['browser'],
            'user_agent': ' '.join(setup['user_agent']),
            'ipv4': ".".join(str(randint(0, 255)) for _ in range(4)),
            'ipv6': ipv6,
            'mac': mac,
        }
