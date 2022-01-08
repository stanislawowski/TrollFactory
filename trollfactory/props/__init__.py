"""Properties generation scripts used by the TrollFactory cli and library."""

from importlib import import_module

__props__: list[str] = [
    'birthdate',
    'gender',
    'language',
    'name',
    'online',
    'address',
]

__all__ = __props__

__attribs__: list[str] = []

for prop in __props__:
    prop_module = import_module('trollfactory.props.'+prop)
    for attrib in getattr(prop_module, prop.capitalize()+'Type'
                          ).__annotations__.keys():
        if attrib != 'prop_title':
            __attribs__.append(attrib)
