from argparse import ArgumentParser
from datetime import datetime
from trollfactory.functions import generate_personality

TROLLFACTORY_VERSION = "2.0.4"
DESCRIPTION = 'Fake personality generator for the 21st century!'


def parse_arguments():
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--amount', dest='amount', type=int, default=1)
    parser.add_argument('--gender', dest='gender', type=str, default='female')
    parser.add_argument(
        '--dataset',
        dest='dataset',
        type=str,
        default='polish')
    parser.add_argument('--no-stdout', dest='stdout', action='store_false')
    parser.add_argument('-v', '--version', action='store_true')
    return parser.parse_args()


def print_line(text, padding=0):
    print('[{}]{} {}'.format(
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        ' ' * padding,
        text
    ))


def print_properties(properties):
    for prop in properties:
        print_line('Prop name: ' + prop)
        for key in properties[prop]:
            print_line(key + ': ' + str(properties[prop][key]), 4)


def main():
    args = parse_arguments()

    if args.version:
        print(TROLLFACTORY_VERSION)
        return

    for _ in range(args.amount):
        personality = generate_personality(args.dataset, args.gender)

        if args.stdout:
            print_properties(personality)


if __name__ == '__main__':
    main()
