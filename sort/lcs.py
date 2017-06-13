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

    m, n = len(X) + 1, len(Y) + 1
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
                    backtrace[i + 1][j + 1] = 1
                else:
                    common_len[i + 1][j + 1] = common_len[i][j + 1]
                    backtrace[i + 1][j + 1] = -1
                    # common_len[i+1][j+1] = max(common_len[i][j+1], common_len[i+1][j])
    # pprint.pprint(common_len)
    # pprint.pprint(backtrace)

    def get_backtrace(bt, m, n, X):
        if m <= 0 or n <=0:
            return None
        stack = [(m, n)]
        common_s = []
        while stack:
            x, y = stack.pop()
            if bt[x][y] == 0:
                common_s.append(X[x - 1])
                if x > 1 and y > 1:
                    stack.append((x - 1, y - 1))
            elif bt[x][y] == -1 and x > 1 and y > 0:
                stack.append((x - 1, y))
            elif bt[x][y] == 1 and x > 0 and y > 1:
                stack.append((x, y - 1))
        return ''.join(common_s[::-1])

    return common_len[m - 1][n - 1], get_backtrace(backtrace, m - 1, n - 1, X)


print get_lcs("abcda", "aca")

# ---------------------------- UT ------------------------------
import unittest


class LCSTest(unittest.TestCase):
    def setUp(self):
        self._test_data = (
            ("", "", 0, None),
            ("a", "", 0, None),
            ("", "b", 0, None),
            ("abcde", "abcde", 5, "abcde"),
            ("abcde", "ae", 2, "ae"),
            ("abcdefgh", "acfgm", 4, "acfg"),
            ("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", 26, "abcdefghijklmnopqrstuvwxyz"),
            ("abcde", "abcde"[::-1], 1, "e")
        )

    def test_get_lcs_with_recursive(self):
        self.assertRaises(TypeError, get_lcs_with_recursive, "abcdef", 12)
        self.assertRaises(TypeError, get_lcs_with_recursive, {}, "abc")

        for i in self._test_data:
            self.assertEqual(i[2], get_lcs_with_recursive(i[0], i[1]))

    def test_get_lcs(self):
        for i in self._test_data:
            lcs, s = get_lcs(i[0], i[1])
            self.assertEqual(i[2], lcs)
            self.assertEqual(i[3], s)


if __name__ == "__main__":
    unittest.main()
