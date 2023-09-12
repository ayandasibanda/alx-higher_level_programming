#!/usr/bin/python3
"""Defines a function to read and print the contents of a text file."""


def read_file(filename=""):
    """Read and print the contents of a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

