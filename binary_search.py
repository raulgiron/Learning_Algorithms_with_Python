from datetime import datetime


def binary_search(data_list: list, target: int) -> int | None:
    """
    Returns the index position of the target if found, else returns None.
    :param data_list:
    :param target:
    :return i:
    """
    first = 0
    last = len(data_list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if data_list[midpoint] == target:
            return midpoint
        elif data_list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index: int) -> None:
    """
    Verifies the index of linear search and print a message.
    :param index:
    """
    start_time = datetime.now()
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list.")
    end_time = datetime.now()
    print("Duration: {}".format(end_time - start_time))


numbers = range(0, 100)
values = list(numbers)
result = binary_search(values, 77)
verify(result)
