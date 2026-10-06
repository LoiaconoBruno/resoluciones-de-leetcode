# 189. Rotate Array (Media)
# https://leetcode.com/problems/rotate-array/
#
# Idea: rotar k a la derecha es dar vuelta todo el array y después dar vuelta por separado los
#       primeros k y el resto.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def invertir(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        invertir(0, n - 1)
        invertir(0, k - 1)
        invertir(k, n - 1)


if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(a, 3)
    assert a == [5, 6, 7, 1, 2, 3, 4]
    a = [-1, -100, 3, 99]
    s.rotate(a, 2)
    assert a == [3, 99, -1, -100]
    a = [1, 2]
    s.rotate(a, 5)
    assert a == [2, 1]
    print("OK")
