#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers in a list.

    Args:
        my_list (list): The list to print integers from.
        x (int): The number of integers from my_list to print.

    Returns:
        The real number of integers printed.
    """
    count = 0  # Initialize a variable to count integers printed
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()  # Print a newline character after printing integers
    except IndexError:
        pass  # Handle the case where x is greater than the list length
    return count  # Return the count of integers printed

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
