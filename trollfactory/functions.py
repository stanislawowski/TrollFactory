from trollfactory import props
from trollfactory.props import *
from trollfactory.exceptions import UnmetDependenciesException
from sys import modules

def generate_personality(p_dataset = 'polish', p_gender = 'female', exclude_props = []):
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
                    if not dependency in properties_static.keys():
                        missing_dependencies = True
                    if dependency not in props.__all__:
                        raise UnmetDependenciesException(
                            'Unmet dependency: ' + dependency
                        )
            if (missing_dependencies): continue

            prop_attrs = prop_class.generate(properties_static)
            properties_static[prop_name] = prop_attrs
            properties.remove(prop_name)

    return properties_static
