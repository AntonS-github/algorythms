"""
Пирамидальная сортировка (сортировка "кучей")
"""


def HeapSift(data, start, end):
    root = start
    while True:
        left_child = root * 2 + 1
        right_child = root * 2 + 2
        if left_child > end:
            break

        if right_child <= end and data[left_child] < data[right_child]:
            left_child += 1

        if data[root] < data[left_child]:
            data[root], data[left_child] = data[left_child], data[root]
            root = left_child
        else:
            break

        HeapSift(list, root, left_child)


def HeapSort(data):
    for start in range((len(data) - 2) // 2, -1, -1):
        HeapSift(data, start, len(data) - 1)

    for end in range(len(data) - 1, 0, -1):
        data[end], data[0] = data[0], data[end]

        HeapSift(data, 0, end - 1)
    return data
