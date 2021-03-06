#!/usr/bin/python3

"""Simple python script to 'pretty' json data.

It attempts to make use of the C based simplejson, but will fall back to using
the core json module if simplejson is not available.

This script can read both data from stdin, or from a stored text file.

"""

import argparse
import os
import sys

try:
    import simplejson as json
except ImportError:
    import json  # pylint: disable=wrong-import-order


def _parser():
    """Parse arguments and return an argparse namespace."""
    # The use of type, default, and nargs allows the stdin/stdout to work,
    # since one would either provide a file or stdin/out data

    # By making output a switched optional argument we can us either a file or
    # stdin for input, and still use either stdout or a file for output
    parser = argparse.ArgumentParser()
    parser.add_argument('input',
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        nargs='?',
                        help='JSON data to pretty. Default: stdin')
    parser.add_argument('-o', '--output',
                        default=None,
                        help='Location to place the updated data. '
                             'Default: stdout')
    parser.add_argument('-i', '--indent',
                        type=int,
                        default=4,
                        help='The number of spaces to indent the file by')
    parser.add_argument('-p', '--preserve',
                        action='store_true',
                        help='Save the original file as a <file>.bak, if '
                             'overwritting. Has no effect if the destination '
                             'is not the same as the input')
    return parser.parse_args()


def main():
    """Main function."""
    args = _parser()
    equal = False

    # True if the input and output are the same
    if args.output is not None:
        equal = os.path.abspath(args.input.name) == os.path.abspath(args.output)

    # Read in the contents of the old data as json data
    # If parsing fails, print a message about the invalid content and exit with
    # a status of 1
    try:
        content = json.load(args.input)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    # If requested save the old file with a .bak extension
    if args.preserve and equal:
        args.input.close()
        os.rename(args.input.name, args.input.name + '.bak')

    # If the output is stdout
    if args.output is not None:
        with open(args.output, 'w') as f:
            json.dump(content, f, indent=args.indent)
    else:
        json.dump(content, sys.stdout, indent=args.indent)


if __name__ == '__main__':
    main()
