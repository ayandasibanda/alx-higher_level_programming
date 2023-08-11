#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1
args = sys.argv[1:]

print("{} argument{}{}".format(num_args, "" if num_args == 1 else "s", ":" if num_args else "."))
for i, arg in enumerate(args):
    print("{}: {}".format(i + 1, arg))

