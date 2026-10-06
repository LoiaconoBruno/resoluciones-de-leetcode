# 167. Two Sum II Input Array Is Sorted (Media)
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#
# Idea: como el array está ordenado, si la suma de las puntas se pasa muevo la derecha y si no llega muevo la izquierda.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        izq, der = 0, len(numbers) - 1
        while izq < der:
            suma = numbers[izq] + numbers[der]
            if suma == target:
                return [izq + 1, der + 1]
            if suma > target:
                der -= 1
            else:
                izq += 1
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([2, 3, 4], 6) == [1, 3]
    assert s.twoSum([-1, 0], -1) == [1, 2]
    print("OK")
