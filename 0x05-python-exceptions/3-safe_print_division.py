#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide two integers and print the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        The result of the division or None if an exception occurs.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
