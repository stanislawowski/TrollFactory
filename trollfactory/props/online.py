"""Online activity data generation prop for TrollFactory."""

from string import ascii_uppercase, ascii_lowercase, digits
from random import choice, randint
from typing import TypedDict, Callable, cast


class OnlineType(TypedDict):
    """Type hint for the online activity data property."""

    prop_title: str
    username: str
    email: str
    receive_email: str
    domain_name: str
    password: str
    operating_system: str
    browser: str
    user_agent: str
    ipv4: str
    ipv6: str
    mac: str


def generate_password() -> str:
    """Generate a password."""
    return ''.join(choice(
        ascii_uppercase+ascii_lowercase+digits) for _ in range(16))


def generate_mac() -> str:
    """Generate a MAC address."""
    return ('02:00:00:%02x:%02x:%02x' % (
            randint(0, 255), randint(0, 255), randint(0, 255))).upper()


class Online:
    """Online activity data generation prop for TrollFactory."""

    def __init__(self, properties: dict, generator: Callable) -> None:
        self.properties = properties
        self.generator: Callable = generator
        self.unresolved_dependencies: list[str] = []

        for dependency in ('name', 'language'):
            if dependency not in self.properties:
                self.unresolved_dependencies.append(dependency)

    def generate(self) -> OnlineType:
        """Generate the online activity data."""
        data: dict[str, str] = {
            'prop_title': 'Online',
            'username': self.generator('username', self.properties),
            'email': self.generator('email', self.properties),
            'domain_name': self.generator('domain_name', self.properties),
            'password': generate_password(),
            'operating_system': self.generator('operating_system',
                                               self.properties),
            'browser': self.generator('browser', self.properties),
            'user_agent': self.generator('user_agent', self.properties),
            'ipv4': self.generator('ipv4', self.properties),
            'ipv6': self.generator('ipv6', self.properties),
            'mac': generate_mac(),
        }

        data['receive_email'] = self.generator(
            'receive_email', dict(self.properties, **{'online': data}))

        return cast(OnlineType, data)
