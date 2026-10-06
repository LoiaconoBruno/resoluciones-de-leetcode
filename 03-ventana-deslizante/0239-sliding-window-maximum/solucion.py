# 239. Sliding Window Maximum (Difícil)
# https://leetcode.com/problems/sliding-window-maximum/
#
# Idea: deque con índices cuyos valores van de mayor a menor; el frente siempre es el máximo de la
#       ventana. Antes de meter un número saco del fondo los menores (ya no van a ser máximo nunca).
# Tiempo: O(n) · Espacio: O(k)

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cola = deque()
        res = []
        for i, n in enumerate(nums):
            while cola and nums[cola[-1]] < n:
                cola.pop()
            cola.append(i)
            if cola[0] == i - k:
                cola.popleft()
            if i >= k - 1:
                res.append(nums[cola[0]])
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert s.maxSlidingWindow([1], 1) == [1]
    print("OK")
