#!/usr/bin/python3
"""Define an object attribute lookup function."""

def lookup(obj):
    """Returns a list of the object's available attributes."""
    return (dir(obj))

