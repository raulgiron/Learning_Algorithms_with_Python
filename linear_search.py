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


def alternative_linear_search(data_list: list, target: int) -> int | None:
    """
    Returns the index position of the target if found, else returns None.
    :param data_list:
    :param target:
    :return i:
    """
    for index, value in enumerate(data_list):
        if value == target:
            return index
    return -1


def verify(index: int) -> None:
    """
    Verifies the index of linear search and print a message.
    :param index:
    """
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list.")


numbers = range(0, 100)
values = list(numbers)
result = linear_search(values, 99)
verify(result)
