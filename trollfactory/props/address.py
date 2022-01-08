"""Address generation prop for TrollFactory."""

from typing import TypedDict, Callable, cast


class AddressType(TypedDict):
    """Type hint for an address property."""

    prop_title: str
    country_code: str
    province: str
    city: str
    postcode: str
    street_name: str
    latitude: float
    longitude: float
    street_number: int


class Address:
    """Address generation prop for TrollFactory."""

    def __init__(self, properties: dict, generator: Callable) -> None:
        self.properties = properties
        self.generator: Callable = generator
        self.unresolved_dependencies: tuple = (
            'language',) if 'language' not in properties else ()

    def generate(self) -> AddressType:
        """Generate the address."""
        data: dict = {
            'prop_title': 'Address',
            'country_code': self.generator('country_code', self.properties),
            'street_number': self.generator('street_number', self.properties),
        }

        data['street_name'] = self.generator(
            'street_name', {'address': data} | self.properties)
        data['latitude'] = self.generator(
            'latitude', {'address': data} | self.properties)
        data['longitude'] = self.generator(
            'longitude', {'address': data} | self.properties)
        data['city'] = self.generator(
            'city', {'address': data} | self.properties)
        data['postcode'] = self.generator(
            'postcode', {'address': data} | self.properties)
        data['province'] = self.generator(
            'province', {'address': data} | self.properties)

        return cast(AddressType, data)
