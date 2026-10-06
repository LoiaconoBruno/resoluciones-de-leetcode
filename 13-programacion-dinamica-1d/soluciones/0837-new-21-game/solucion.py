# 837. New 21 Game (Media)
# https://leetcode.com/problems/new-21-game/
#
# Idea: prob[i] = probabilidad de tener exactamente i puntos; llego a i desde cualquier i - x (1 ≤ x
#       ≤ maxPts) mientras ese i - x sea < k (todavía saco cartas). Mantengo la suma de esa ventana
#       para no recalcularla.
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        prob = [1.0] + [0.0] * n
        ventana = 1.0
        res = 0.0
        for i in range(1, n + 1):
            prob[i] = ventana / maxPts
            if i < k:
                ventana += prob[i]
            else:
                res += prob[i]
            if i - maxPts >= 0 and i - maxPts < k:
                ventana -= prob[i - maxPts]
        return res


if __name__ == "__main__":
    s = Solution()
    assert abs(s.new21Game(10, 1, 10) - 1.0) < 1e-5
    assert abs(s.new21Game(6, 1, 10) - 0.6) < 1e-5
    assert abs(s.new21Game(21, 17, 10) - 0.73278) < 1e-5
    print("OK")
