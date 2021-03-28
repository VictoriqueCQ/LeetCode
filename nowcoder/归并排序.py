from typing import List


def merge(a: List[int], b: List[int]):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def sorts(data: List[int]):
    length = len(data)
    if length <= 1: return data
    mid = length // 2
    a = sorts(data[:mid])
    b = sorts(data[mid:])

    return merge(a, b)


data = [1, 4, 2, 5, 6, 7]
print(sorts(data))
# data = [1, 3, 2, 4]


# def merge(a, b):
#     result = []
#     i = 0
#     j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             result.append(a[i])
#             i = i + 1
#         else:
#             result.append(b[j])
#             j = j + 1
#     result.extend(a[i:])
#     result.extend(b[j:])
#     return result
#
#
# def sorts(data):
#     length = len(data)
#     if length <= 1:
#         return data
#     mid = length // 2
#     a = sorts(data[:mid])
#     b = sorts(data[mid:])
#     return merge(a, b)


# sort_data = sorts(data);

# print(sorts(data))
