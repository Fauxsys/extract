#!/usr/bin/env python3
import argparse
import re

""" Extract parameters from a URL. """


def argument_parser() -> argparse.Namespace:
    """ Retrieve the URL. """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Extract parameters from a URL. Python 3.8+ Required.',
        epilog="Example: ./extract --url 'https://www.thisurl.com/get?param1=value1&param2=value2'",
    )
    parser.add_argument(
        '--url',
        required=True,
        help='URL including query',
        dest='url',
    )

    return parser.parse_args()


def extract_url_parameters(url) -> dict:
    """ Extract the URL parameters. """
    # Everything before '?' will be assigned to `_`. Everything afterwards will be assigned to `parameter_list`.
    # '&' and '=' will be removed from the string, so `parameter_list` will only contain keys and values.
    _, *parameter_list = re.split(pattern='[?&=]', string=url)
    # zip will exhaust the `parameter_iterator` variable into (key, value) pairs, and dict will exhaust the zip object.
    # This equates to `dict([(key, value), (key, value), ...])`
    parameters = dict(zip(parameter_iterator := iter(parameter_list), parameter_iterator))
    return parameters


def main() -> None:
    """ Execute the program. """
    args = argument_parser()
    params = extract_url_parameters(url=args.url)
    print(f'{args.url} contains the following parameters: {params}')


if __name__ == '__main__':
    main()
