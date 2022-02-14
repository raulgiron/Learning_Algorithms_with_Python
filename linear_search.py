from datetime import datetime


def linear_search(data_list: list, target: int) -> int | None:
    """
    Returns the index position of the target if found, else returns None.
    :param data_list:
    :param target:
    :return i:
    """
    start_time = datetime.now()
    for i in range(0, len(data_list)):
        if data_list[i] == target:
            return i
    end_time = datetime.now()
    print("Duration: {}".format(end_time - start_time))
    return None


def alternative_linear_search(data_list: list, target: int) -> int | None:
    """
    Returns the index position of the target if found, else returns None.
    :param data_list:
    :param target:
    :return i:
    """
    start_time = datetime.now()
    for index, value in enumerate(data_list):
        if value == target:
            return index
    end_time = datetime.now()
    print("Duration: {}".format(end_time - start_time))
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
result = linear_search(values, 77)
verify(result)
