"""Functions used by the TrollFactory cli and library."""

from sys import modules
from typing import Optional, List
from trollfactory import props
from trollfactory.props import *
from trollfactory.props import langs
from trollfactory.exceptions import UnmetDependenciesException, \
                                    InvalidGenderException, \
                                    UnsupportedDatasetException


def generate_personality(
        p_dataset: str = 'polish',
        p_gender: str = 'female',
        exclude_props: Optional[List[str]] = None) -> dict:
    """Generate a fake personality."""
    exclude_props = exclude_props or []

    if p_gender not in ['female', 'male']:
        raise InvalidGenderException(
            str(p_gender) + ' gender is not supported by TrollFactory yet',
        )

    if p_dataset not in langs.__all__:
        raise UnsupportedDatasetException(
            str(p_dataset) + ' dataset is not supported by TrollFactory yet',
        )

    properties_static = {
        'language': {
            'language': p_dataset
        },
        'gender': {
            'gender': p_gender
        }
    }

    properties = [i for i in props.__all__]

    for prop in exclude_props:
        properties.remove(prop)

    while len(properties) > 0:
        for prop_name in properties:
            prop = modules['trollfactory.props.' + prop_name]
            prop_class = getattr(prop, prop_name.capitalize())

            missing_dependencies = False

            if hasattr(prop_class, 'dependencies'):
                for dependency in prop_class.dependencies:
                    if dependency not in properties_static.keys():
                        missing_dependencies = True
                    if dependency not in props.__all__:
                        raise UnmetDependenciesException(
                            'Unmet dependency: ' + dependency,
                        )
            if missing_dependencies:
                continue

            prop_attrs = prop_class.generate(properties_static)
            properties_static[prop_name] = prop_attrs
            properties.remove(prop_name)

    return properties_static
