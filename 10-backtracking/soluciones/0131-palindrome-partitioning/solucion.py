# 131. Palindrome Partitioning (Media)
# https://leetcode.com/problems/palindrome-partitioning/
#
# Idea: desde la posición i pruebo cada corte s[i:j] que sea palíndromo y sigo particionando el
#       resto desde j.
# Tiempo: O(n · 2^n) · Espacio: O(n) de recursión

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        actual = []

        def cortar(i):
            if i == len(s):
                res.append(actual[:])
                return
            for j in range(i + 1, len(s) + 1):
                pedazo = s[i:j]
                if pedazo == pedazo[::-1]:
                    actual.append(pedazo)
                    cortar(j)
                    actual.pop()

        cortar(0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.partition("aab")) == [["a", "a", "b"], ["aa", "b"]]
    assert s.partition("a") == [["a"]]
    print("OK")
