"""Functions used by the TrollFactory cli and library."""

from sys import modules
from importlib import import_module
from types import ModuleType

from trollfactory import props
from trollfactory.exceptions import (
    UnmetDependenciesException,
    UnsupportedDatasetException,
)


def import_dataset(dataset: str) -> ModuleType:
    """Import dataset module."""
    try:
        return import_module('trollfactory_'+dataset)
    except ModuleNotFoundError as error:
        raise UnsupportedDatasetException(
            str(dataset)+' dataset not found!') from error


def generate_personality(dataset: str = 'pl_PL', exclude: tuple = (),
                         static: dict = {}) -> dict:
    """Generate a fake personality."""
    assert len(dataset.split('_')) == 2, 'Invalid dataset name format!'
    generator = getattr(import_dataset(dataset), 'generate_property')

    generated = dict(static)

    if 'language' not in generated:
        generated['language'] = {}

    if 'dataset' not in generated['language']:
        generated['language']['dataset'] = dataset

    properties: list[str] = [i for i in props.__props__ if i not in exclude]

    while len(properties) > 0:
        for prop_name in properties:
            prop_class = getattr(modules['trollfactory.props.'+prop_name],
                                 ''.join([i.capitalize()
                                          for i in prop_name.split('_')]))(
                                          generated, generator)

            if len(prop_class.unresolved_dependencies):
                for dependency in prop_class.unresolved_dependencies:
                    if dependency not in props.__props__:
                        raise UnmetDependenciesException(
                            'Unmet dependency: '+dependency)
            else:
                generated_property = prop_class.generate()
                if generated_property:
                    generated[prop_name] = generated_property
                properties.remove(prop_name)

    return generated
