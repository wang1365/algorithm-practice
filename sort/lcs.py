import pprint


def get_lcs_with_recursive(X, Y):
    def lcs(X, xn, Y, yn):
        if xn <= 0 or yn <= 0:
            return 0

        if X[xn - 1] == Y[yn - 1]:
            return lcs(X, xn - 1, Y, yn - 1) + 1

        return max(lcs(X, xn - 1, Y, yn), lcs(X, xn, Y, yn - 1))

    if not isinstance(X, (list, tuple, str)) or not isinstance(Y, (list, tuple, str)):
        raise TypeError("X and Y must be list, tuple or str")

    return lcs(X, len(X), Y, len(Y))


def get_lcs(X, Y):
    if not isinstance(X, (list, tuple, str)) or not isinstance(Y, (list, tuple, str)):
        raise TypeError("X and Y must be list, tuple or str")

    m, n = len(X)+1, len(Y)+1
    common_len = [[0 for j in range(n)] for i in range(m)]
    backtrace = [[0 for j in range(n)] for i in range(m)]
    pprint.pprint(common_len)

    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                common_len[i + 1][j + 1] = common_len[i][j] + 1
            else:
                if common_len[i + 1][j] >= common_len[i][j + 1]:
                    common_len[i + 1][j + 1] = common_len[i + 1][j]
                    backtrace[i+1][j+1] = 1
                else:
                    common_len[i + 1][j + 1] = common_len[i][j + 1]
                    backtrace[i+1][j+1] = -1
                    # common_len[i+1][j+1] = max(common_len[i][j+1], common_len[i+1][j])
    pprint.pprint(common_len)
    pprint.pprint(backtrace)

    return common_len, backtrace


def backtrace(bt, m, n, X):
    if m == 0 or n == 0:
        return

    if bt[m][n] == 0:
        print "*" + X[m-1],
        backtrace(bt, m - 1, n - 1, X)
    elif bt[m][n] == -1:
        backtrace(bt, m - 1, n, X)
    else:
        backtrace(bt, m, n - 1, X)


cl, bt = get_lcs("abcda", "aca")
backtrace(bt, 5, 3, "abcda")

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
        self.assertRaises(TypeError, get_lcs_with_recursive, "abcdef", 12)
        self.assertRaises(TypeError, get_lcs_with_recursive, {}, "abc")

        for i in self._test_data:
            self.assertEqual(i[2], get_lcs_with_recursive(i[0], i[1]))


if __name__ == "__main__":
    unittest.main()
