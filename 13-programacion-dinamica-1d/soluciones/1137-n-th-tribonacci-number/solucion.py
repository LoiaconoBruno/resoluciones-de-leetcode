# 1137. N-th Tribonacci Number (Fácil)
# https://leetcode.com/problems/n-th-tribonacci-number/
#
# Idea: como Fibonacci pero sumando los tres anteriores; guardo solo los últimos tres.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a


if __name__ == "__main__":
    s = Solution()
    assert s.tribonacci(4) == 4
    assert s.tribonacci(25) == 1389537
    assert s.tribonacci(0) == 0
    print("OK")
