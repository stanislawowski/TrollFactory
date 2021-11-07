"""Online activity data generation prop for TrollFactory."""

from string import ascii_uppercase, ascii_lowercase, digits
from random import choice, randint
from pkgutil import get_data
from typing import Optional, TypedDict
from json import loads

EMAIL_PROVIDERS: dict[str, list[str]] = {
    'polish': ['@niepodam.pl'],
    'english_us': ['@armyspy.com', '@cuvox.de', '@dayrep.com', '@einrot.com',
                   '@gustr.com', '@jourrapide.com', '@rhyta.com',
                   '@superrito.com', '@teleworm.us'],
}

EMAIL_URLS: dict[str, str] = {
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

TLDS: list[str] = ['.pl', '.com', '.com.pl', '.net', '.biz', '.me']


class OnlineType(TypedDict):
    """Type hint for the online activity data property."""

    prop_title: str
    username: str
    email: str
    receive_email: Optional[str]
    domain_name: str
    password: str
    operating_system: str
    browser: str
    user_agent: str
    ipv4: str
    ipv6: str
    mac: str


def generate_username(name: str, surname: str) -> str:
    """Generate a username."""
    name = name.split(', ')[0] if ', ' in name else name
    return name.lower()[0] + '_' + surname.lower()


def generate_email(username: str, language: str) -> str:
    """Generate an e-mail address."""
    return username + choice(EMAIL_PROVIDERS[language])


def generate_email_url(email: str, username: str) -> Optional[str]:
    """Generate an online e-mail client URL."""
    email_provider: str = '@' + email.split('@')[1]
    if email_provider in EMAIL_URLS:
        return EMAIL_URLS[email_provider] + username
    return None


def generate_domain_name(username: str) -> str:
    """Generate a domain name."""
    return username.replace('_', '') + choice(TLDS)


def generate_password() -> str:
    """Generate a password."""
    return ''.join(choice(ascii_uppercase + ascii_lowercase + digits
                          ) for _ in range(16))


def generate_setup(language: str) -> dict:
    """Generate a dict with computer setup data."""
    return choice(loads(get_data(__package__,
                                 'langs/'+language+'/setups.json')))


def generate_operating_system(setup: dict) -> str:
    """Generate an operating system."""
    return setup['os']


def generate_browser(setup: dict) -> str:
    """Generate a web browser."""
    return setup['browser']


def generate_user_agent(setup: dict) -> str:
    """Generate a user-agent string."""
    return ' '.join(setup['user_agent'])


def generate_ipv4() -> str:
    """Generate an IPv4 address."""
    return '.'.join(str(randint(0, 255)) for _ in range(4))


def generate_ipv6() -> str:
    """Generate an IPv6 address."""
    return ':'.join('{:x}'.format(randint(0, 2**16 - 1)) for i in range(8))


def generate_mac() -> str:
    """Generate a MAC address."""
    return ("02:00:00:%02x:%02x:%02x" % (
            randint(0, 255), randint(0, 255), randint(0, 255))).upper()


class Online:
    """Online activity data generation prop for TrollFactory."""

    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies: list[str] = []

        for dependency in ['name', 'language']:
            if dependency not in self.properties:
                self.unresolved_dependencies.append(dependency)

    def generate(self) -> OnlineType:
        """Generate the online activity data."""
        # Used properties
        name: str = self.properties['name']['name']
        surname: str = self.properties['name']['surname']
        language: str = self.properties['language']['language']

        # Generate data
        username: str = generate_username(name, surname)
        email: str = generate_email(username, language)
        domain_name: str = generate_domain_name(username)
        password: str = generate_password()
        setup: dict = generate_setup(language)
        operating_system: str = generate_operating_system(setup)
        browser: str = generate_browser(setup)
        user_agent: str = generate_user_agent(setup)
        ipv4: str = generate_ipv4()
        ipv6: str = generate_ipv6()
        mac: str = generate_mac()
        email_url: Optional[str] = generate_email_url(email, username)

        return {
            'prop_title': 'Online',
            'username': username,
            'email': email,
            'receive_email': email_url,
            'domain_name': domain_name,
            'password': password,
            'operating_system': operating_system,
            'browser': browser,
            'user_agent': user_agent,
            'ipv4': ipv4,
            'ipv6': ipv6,
            'mac': mac,
        }
