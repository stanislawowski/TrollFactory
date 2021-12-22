"""Properties generation scripts used by the TrollFactory cli and library."""

from importlib import import_module

__props__: list[str] = [
    'birthdate',
    'gender',
    'language',
    'name',
]

__all__ = __props__

for prop in __props__:
    import_module('trollfactory.props.'+prop)
