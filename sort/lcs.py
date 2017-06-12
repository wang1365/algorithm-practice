def get_lcs_with_recursive(X, Y):
    def lcs(X, xn, Y, yn):
        if xn <= 0 or yn <= 0:
            return 0

        if X[xn - 1] == Y[yn - 1]:
            return lcs(X, xn - 1, Y, yn - 1) + 1

        return max(lcs(X, xn - 1, Y, yn), lcs(X, xn, Y, yn - 1))

    if not isinstance(X, (list, tuple, str)) or not isinstance(Y, (list, tuple, str)):
        raise TypeError("X and Y must be list or tuple")

    return lcs(X, len(X), Y, len(Y))


# ---------------------------- UT ------------------------------
import unittest


class LCSTest(unittest.TestCase):
    def setUp(self):
        self._test_data = (
            ("", "", 0),
            ("a", "", 0),
            ("", "b", 0),
            ("abcde", "abcde", 5),
            ("abcde", "ae", 2),
            ("abcdefgh", "acfhgm", 4),
            ("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", 26),
            ("abcde", "abcde"[::-1], 1)
        )

    def test_get_lcs_with_recursive(self):
        for i in self._test_data:
            assert i[2] == get_lcs_with_recursive(i[0], i[1])


if __name__ == "__main__":
    unittest.main()
