# 219. Contains Duplicate II (Fácil)
# https://leetcode.com/problems/contains-duplicate-ii/
#
# Idea: mantengo en un set los últimos k números (la ventana); si el que entra ya está en el set,
#       hay un duplicado a distancia ≤ k.
# Tiempo: O(n) · Espacio: O(k)

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ventana = set()
        for i, n in enumerate(nums):
            if n in ventana:
                return True
            ventana.add(n)
            if len(ventana) > k:
                ventana.remove(nums[i - k])
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert s.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
    print("OK")
