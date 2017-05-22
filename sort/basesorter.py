class BaseSorter(object):
    def sort(self, data):
        raise NotImplementedError("sort method should be implemented")


def sort(data, sorter):
    sorter().sort(data)
