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
            str(p_gender) + ' gender is not supported by TrollFactory yet')

    if p_dataset not in langs.__all__:
        raise UnsupportedDatasetException(
            str(p_dataset) + ' dataset is not supported by TrollFactory yet')

    properties_static = {
        'language': {'language': p_dataset},
        'gender': {'gender': p_gender},
    }

    properties = [i for i in props.__all__]

    for prop in exclude_props:
        properties.remove(prop)

    while len(properties) > 0:
        for prop_name in properties:
            prop_class = getattr(modules['trollfactory.props.'+prop_name],
                                 ''.join([i.capitalize()
                                          for i in prop_name.split('_')]))(
                                          properties_static)

            if len(prop_class.unresolved_dependencies):
                for dependency in prop_class.unresolved_dependencies:
                    if dependency not in props.__all__:
                        raise UnmetDependenciesException(
                            'Unmet dependency: '+dependency)
            else:
                generated_property = prop_class.generate()
                if generated_property:
                    properties_static[prop_name] = generated_property
                properties.remove(prop_name)

    return properties_static
