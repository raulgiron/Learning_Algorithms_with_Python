from datetime import datetime


def linear_search(data_list: list, target: int) -> int | None:
    """
    Returns the index position of the target if found, else returns None.
    :param data_list:
    :param target:
    :return i:
    """

    for i in range(0, len(data_list)):
        if data_list[i] == target:
            return i
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


numbers = range(0, 10)
values = list(numbers)
result = linear_search(values, 9)
verify(result)
