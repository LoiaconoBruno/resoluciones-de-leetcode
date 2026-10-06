# 1899. Merge Triplets to Form Target Triplet (Media)
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
#
# Idea: una tripleta con algún valor mayor que el del target la arruina, así que la descarto. Con
#       las que quedan, alcanza con que entre todas logren cada uno de los tres valores exactos.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        logrados = set()
        for t in triplets:
            if all(t[i] <= target[i] for i in range(3)):
                for i in range(3):
                    if t[i] == target[i]:
                        logrados.add(i)
        return len(logrados) == 3


if __name__ == "__main__":
    s = Solution()
    assert s.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]) is True
    assert s.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]) is False
    assert s.mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]) is True
    print("OK")
