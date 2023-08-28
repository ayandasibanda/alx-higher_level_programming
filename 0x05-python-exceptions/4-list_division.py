#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element in two lists and handle exceptions.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The length of the new list.

    Returns:
        A new list with divisions.
    """
    result = []

    for i in range(list_length):
        try:
            dividend = my_list_1[i] if i < len(my_list_1) else 0
            divisor = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                if divisor == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(dividend / divisor)
            else:
                result.append(0)
                print("wrong type")

        except (IndexError):
            print("out of range")
            result.append(0)

    return result

if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
