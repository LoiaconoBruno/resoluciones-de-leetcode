# 1822. Sign of An Array (Fácil)
# https://leetcode.com/problems/sign-of-the-product-of-an-array/
#
# Idea: no hace falta multiplicar: si hay un 0 el signo es 0; si no, depende de si la cantidad de negativos es par o impar.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negativos = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                negativos += 1
        return -1 if negativos % 2 else 1


if __name__ == "__main__":
    s = Solution()
    assert s.arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1
    assert s.arraySign([1, 5, 0, 2, -3]) == 0
    assert s.arraySign([-1, 1, -1, 1, -1]) == -1
    print("OK")
