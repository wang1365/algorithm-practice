from sort.basesorter import BaseSorter
import math
import os


class HeapSort(BaseSorter):
    def sort(self, data):
        if not isinstance(data, list):
            raise TypeError("Only support list type")
        self._data = data
        self._end = len(data) - 1
        print "Original data:", data
        print "Original data in heap style:"
        self.print_heap(data)

        print "Initial heap:"
        self._init_heap()
        self.print_heap(data)

        print "Sorted heap:"
        self._sort_heap()
        self.print_heap(data)

    def _init_heap(self):
        start, end = len(self._data) / 2 - 1, 0
        for i in range(start, end - 1, -1):
            self._adjust_node(i, self._end)

    def _sort_heap(self):
        for i in range(len(self._data)-1, -1, -1):
            self._data[0], self._data[i] = self._data[i], self._data[0]
            self._adjust_node(0, i-1)

    def _adjust_node(self, index, end):
        tmp = self._data[index]
        parent, biggerchild = index, 2 * index + 1
        while biggerchild <= end:
            if biggerchild + 1 < end and self._data[biggerchild] < self._data[biggerchild + 1]:
                biggerchild += 1
            if tmp >= self._data[biggerchild]:
                break

            self._data[parent] = self._data[biggerchild]
            parent = biggerchild
            biggerchild = 2 * parent + 1

        self._data[parent] = tmp

    @staticmethod
    def print_heap(data):
        for index, item in enumerate(data):
            print item,
            if index + 1 == 2 ** HeapSort.height_of_heap(nodecount=index + 1) - 1:
                print os.linesep
        print os.linesep

    @staticmethod
    def height_of_heap(nodecount):
        return int(math.floor(math.log(nodecount + 1, 2)))


if __name__ == '__main__':
    data = [i for i in range(100)]
    import random

    random.shuffle(data)
    HeapSort().sort(data)
