import math
import os


def sort(data):
    if not isinstance(data, list):
        raise TypeError("Only support list type")

    print "Initial heap:"
    init_heap()

    print "Sorted heap:"
    _sort_heap()


def init_heap(data):
    start, end = len(data) / 2 - 1, 0
    for i in range(start, end - 1, -1):
        adjust_node(i, end)


def _sort_heap(data):
    for i in range(len(data) - 1, -1, -1):
        data[0], data[i] = data[i], data[0]
        adjust_node(0, i - 1)


def adjust_node(data, index, end):
    tmp = data[index]
    parent, biggerchild = index, 2 * index + 1
    while biggerchild <= end:
        if biggerchild + 1 <= end and data[biggerchild] < data[biggerchild + 1]:
            biggerchild += 1
        if tmp >= data[biggerchild]:
            break

        data[parent] = data[biggerchild]
        parent = biggerchild
        biggerchild = 2 * parent + 1

        data[parent] = tmp


def print_heap(data):
    for index, item in enumerate(data):
        print item,
        if index + 1 == 2 ** height_of_heap(nodecount=index + 1) - 1:
            print os.linesep
    print os.linesep


def height_of_heap(nodecount):
    return int(math.floor(math.log(nodecount + 1, 2)))


# ---------------- UT -------------

import pytest

testdata = [
    (1, 1),
    (2, 2), (3, 2),
    (4, 3), (5, 3), (6, 3), (7, 3)

]


@pytest.mark.parametrize("nodecount, expected", testdata)
def test_height_of_heap(nodecount, expected):
    assert height_of_heap(nodecount) == expected
