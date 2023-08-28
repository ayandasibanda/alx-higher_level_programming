#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """Execute a function safely and handle exceptions.

    Args:
        fct (function): The function to execute.
        *args: Any arguments to pass to the function.

    Returns:
        The result of the function if successful, None otherwise.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
