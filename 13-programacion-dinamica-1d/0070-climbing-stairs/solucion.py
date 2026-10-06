# 70. Climbing Stairs (Fácil)
# https://leetcode.com/problems/climbing-stairs/
#
# Idea: para llegar al escalón n vengo del n - 1 o del n - 2, así que formas(n) = formas(n - 1) +
#       formas(n - 2): es Fibonacci. Alcanza con guardar los dos últimos.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(5) == 8
    assert s.climbStairs(1) == 1
    print("OK")
