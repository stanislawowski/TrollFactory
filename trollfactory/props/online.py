"""Online activity data generation prop for TrollFactory."""

from string import ascii_uppercase, ascii_lowercase, digits
from random import choice, randint
from typing import TypedDict, Callable, cast

DEPENDENCIES = (('name', 'surname'), ('name', 'name'),
                ('language', 'language'))


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

        for dependency in DEPENDENCIES:
            if dependency[0] not in self.properties \
                    or dependency[1] not in self.properties[dependency[0]]:
                self.unresolved_dependencies.append(dependency[0])

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
            'ipv4': self.generator('ipv4', self.properties),
            'ipv6': self.generator('ipv6', self.properties),
            'mac': generate_mac(),
        }

        if 'online' in self.properties \
                and 'receive_email' in self.properties['online']:
            data['receive_email'] = self.properties['online']['receive_email']

        data['receive_email'] = self.generator('receive_email',
                                               {'online': data})
        data['browser'] = self.generator('browser',
                                         {'online': data} | self.properties)
        data['user_agent'] = self.generator('user_agent',
                                            {'online': data} | self.properties)

        return cast(OnlineType, data)
