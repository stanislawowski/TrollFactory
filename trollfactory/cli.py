"""TrollFactory cli functions."""

from typing import Any
from argparse import ArgumentParser, Namespace
from datetime import datetime

from trollfactory import TROLLFACTORY_VERSION, DESCRIPTION
from trollfactory.functions import generate_personality


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
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]{" "*padding}',
          f'{text}')


def print_properties(properties: dict) -> None:
    """Print generated properties."""
    for prop in properties:
        print_line('Prop name: '+prop)

        for key in properties[prop]:
            if isinstance(properties[prop][key], dict):
                print_line(key+':', 4)
                for key1 in properties[prop][key]:
                    print_line(key1+': '+str(properties[prop][key][key1]), 8)
            else:
                print_line(key+': '+str(properties[prop][key]), 4)


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
