#!/usr/bin/python3

"""Simple python script to 'pretty' json files.

It attempts to make use of the C based simplejson, but will fall back to using
the core json module if simplejson is not available.

"""

import argparse
import os

try:
    import simplejson as json
except ImportError:
    import json


def _parser():
    """Parse arguments and return an argparse namespace."""
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='A JSON file to clean')
    parser.add_argument('-i', '--indent',
                        type=int,
                        default=4,
                        help='The number of spaces to indent the file by')
    parser.add_argument('-p', '--preserve',
                        action='store_true',
                        help='Save the original file as a <file>.bak')
    return parser.parse_args()


def main():
    """Main function."""
    args = _parser()

    # Read in the contents of the old file as json data
    with open(args.file, 'r') as f:
        content = json.load(f)

    # If requested save the old file with a .bak extension
    if args.preserve:
        os.rename(args.file, args.file + '.bak')

    # Finally dump the updated file
    with open(args.file, 'w') as f:
        json.dump(content, f, indent=args.indent)


if __name__ == '__main__':
    main()
