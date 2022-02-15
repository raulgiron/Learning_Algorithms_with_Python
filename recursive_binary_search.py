def recursive_binary_search(data_list, target):
    if len(data_list) == 0:
        return False
    else:
        midpoint = (len(data_list)) // 2

        if data_list[midpoint] == target:
            return True
        else:
            if data_list[midpoint] < target:
                return recursive_binary_search(data_list[midpoint + 1:], target)
            else:
                return recursive_binary_search(data_list[:midpoint], target)


def alternative_recursive_binary_search(data_list: list, target: int, start: int = 0, end=None) -> int | None:
    if end is None:
        end = len(data_list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == data_list[mid]:
        return mid
    else:
        if target < data_list[mid]:
            return alternative_recursive_binary_search(data_list, target, start, mid - 1)
        else:
            return alternative_recursive_binary_search(data_list, target, mid + 1, end)


def sum_values(data_list):
    if len(data_list) == 1:
        return data_list[0]
    else:
        return data_list[0] + sum_values(data_list[1:])


def verify(result):
    print("Target found: ", result)


def sum_verify(result):
        print("The sum is: ", result)



empty_list = []
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(numbers_list, 12)
verify(result)
result = recursive_binary_search(numbers_list, 6)
verify(result)
result = alternative_recursive_binary_search(numbers_list, 12)
verify(result)
result = alternative_recursive_binary_search(numbers_list, 6)
verify(result)
result = sum_values(numbers_list)
sum_verify(result)
