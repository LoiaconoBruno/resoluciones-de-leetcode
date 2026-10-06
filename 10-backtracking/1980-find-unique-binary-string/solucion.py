# 1980. Find Unique Binary String (Media)
# https://leetcode.com/problems/find-unique-binary-string/
#
# Idea: diagonal de Cantor: armo un string que difiere de nums[i] en la posición i (doy vuelta ese
#       bit). Así es distinto de cada uno de los n strings.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join("1" if nums[i][i] == "0" else "0" for i in range(len(nums)))


if __name__ == "__main__":
    s = Solution()
    for nums in (["01", "10"], ["00", "01"], ["111", "011", "001"], ["0"]):
        r = s.findDifferentBinaryString(nums)
        assert len(r) == len(nums) and r not in nums
    print("OK")
