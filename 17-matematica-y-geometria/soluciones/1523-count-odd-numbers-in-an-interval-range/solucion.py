# 1523. Count Odd Numbers in an Interval Range (Fácil)
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
#
# Idea: entre 1 y x hay (x + 1) // 2 impares; los impares de [low, high] son los de hasta high menos
#       los de hasta low - 1.
# Tiempo: O(1) · Espacio: O(1)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


if __name__ == "__main__":
    s = Solution()
    assert s.countOdds(3, 7) == 3
    assert s.countOdds(8, 10) == 1
    assert all(s.countOdds(a, b) == sum(x % 2 for x in range(a, b + 1)) for a in range(20) for b in range(a, 20))
    print("OK")
