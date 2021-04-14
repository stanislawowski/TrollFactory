#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from os.path import basename, isfile, join
from datetime import datetime
from glob import glob
from argparse import ArgumentParser
from json import loads, dumps

parser = ArgumentParser(description='Fake identities generator.')
parser.add_argument('--amount', dest='amount', type=int, default=1)
parser.add_argument('--sex', dest='sex', type=str, default='male')
parser.add_argument('--dataset', dest='dataset', type=str, default='polish')
parser.add_argument('-o', '--output', dest='file', type=str)
parser.add_argument('--no-stdout', dest='stdout', action='store_false')
args = parser.parse_args()
sex = args.sex
dataset = args.dataset

def output(text):
    print('[{}] {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), text))

def save_to_file(properties, file):
    with open(file, 'a') as f:
        f.write(dumps(properties))

def load_props(props = None):
    if (not props):
        modules = glob(join('props', "*.py"))
        __all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
    return __all__

def print_properties(properties):
    properties['online']['user_agent'] = ("\n"+38*" ").join(properties['online']['user_agent'])
    for prop in properties:
        output('Prop name: ' + prop)
        for key in properties[prop]:
            if (properties[prop][key] != None):
                output('    ' + key + ': ' + str(properties[prop][key]))

def generate(dataset, sex):
    properties = load_props()
    country_code = {'polish': 'PL', 'english_us': 'US'}[dataset]
    properties_static = {'language': {'language': dataset, 'country_code': country_code}, 'sex': {'sex': sex}}

    while len(properties) > 0:
        for prop_name in properties:

            prop = __import__('props.'+prop_name)
            prop_class = getattr(getattr(prop, prop_name), prop_name.capitalize())

            missing_dependencies = False
            
            if hasattr(prop_class, 'dependencies'):
                for dependency in prop_class.dependencies:
                    if not dependency.lower() in properties_static.keys():
                        missing_dependencies = True
            if (missing_dependencies): continue
            
            prop_attrs = prop_class.generate(properties_static)
            
            properties_static[prop_name] = prop_attrs
            properties.remove(prop_name)
    
    return properties_static

if __name__ == '__main__':
    output('Starting TrollFactory..\n')
    for _ in range(args.amount):
        properties = load_props()
        generated = generate(dataset, sex)

        if args.stdout:
            print_properties(generated)
        if args.file:
            save_to_file(generated, args.file)
