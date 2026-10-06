# 1470. Shuffle the Array (Fácil)
# https://leetcode.com/problems/shuffle-the-array/
#
# Idea: como los valores entran en 10 bits, guardo dos números en una misma casilla: en nums[i] meto
#       también nums[i + n] corrido 10 bits. Después lleno el array desde el final desarmando cada
#       par, sin espacio extra.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] |= nums[i + n] << 10
        for i in range(n - 1, -1, -1):
            x, y = nums[i] & 1023, nums[i] >> 10
            nums[2 * i] = x
            nums[2 * i + 1] = y
        return nums


if __name__ == "__main__":
    s = Solution()
    assert s.shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
    assert s.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert s.shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]
    print("OK")
