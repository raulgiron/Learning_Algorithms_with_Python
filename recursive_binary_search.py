def recursive_binary_search(data_list, target):
    if len(data_list) == 0:
        return False
    else:
        midpoint = (len(data_list)) // 2

        if data_list[midpoint] == target:
            return True
        else:
            if data_list[midpoint] < target:
                return recursive_binary_search(data_list[midpoint+1:], target)
            else:
                return recursive_binary_search(data_list[:midpoint], target)


def verify(result):
    print("Target found: ", result)


numbers1 = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers1, 6)
verify(result)
result = recursive_binary_search(numbers, 12)
verify(result)
result = recursive_binary_search(numbers, 6)
verify(result)
