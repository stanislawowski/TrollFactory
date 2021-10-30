"""TrollFactory cli functions."""

from typing import Any
from argparse import ArgumentParser, Namespace
from datetime import datetime
from trollfactory.functions import generate_personality

TROLLFACTORY_VERSION: str = '2.1.2'
DESCRIPTION: str = 'Fake personality generator for the 21st century!'


def parse_arguments() -> Namespace:
    """Parse command-line arguments."""
    parser: ArgumentParser = ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        '--amount',
        dest='amount',
        type=int,
        default=1,
        help='a number of personalities to generate',
    )

    parser.add_argument(
        '--gender',
        dest='gender',
        type=str,
        default='female',
        help='generated personalities\' gender',
    )

    parser.add_argument(
        '--dataset',
        dest='dataset',
        type=str,
        default='polish',
        help='the name of the dataset to be used',
    )

    parser.add_argument(
        '--no-stdout',
        dest='stdout',
        action='store_false',
        help='don\'t display the generated personalities',
    )

    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help='show TrollFactory version and exit',
    )

    return parser.parse_args()


def print_line(text: str, padding: int = 0) -> None:
    """Print a formatted line."""
    print('[{}]{} {}'.format(
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        ' ' * padding,
        text,
    ))


def print_properties(properties: dict) -> None:
    """Print generated properties."""
    for prop in properties:
        print_line('Prop name: ' + prop)

        for key in properties[prop]:
            print_line(key + ': ' + str(properties[prop][key]), 4)


def main() -> None:
    """Run the cli."""
    args: Namespace = parse_arguments()

    if args.version:
        print(TROLLFACTORY_VERSION)
        return

    for _ in range(args.amount):
        personality: dict[str, Any] = generate_personality(args.dataset,
                                                           args.gender)

        if args.stdout:
            print_properties(personality)


if __name__ == '__main__':
    main()
