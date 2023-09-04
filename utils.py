from typing import List


def print_array(arr):
    res = "["
    i = 1

    for x in arr:
        res += "'{}'".format(x)

        if i < len(arr):
            res += ","
        i += 1

    res += "]"

    return res


def create_list_of_length(list_length: List[int]) -> List[int]:
    return [x for x in range(1, list_length + 1)]
