# 2140. Solving Questions With Brainpower (Media)
# https://leetcode.com/problems/solving-questions-with-brainpower/
#
# Idea: de atrás para adelante: dp[i] = máximo entre saltear la pregunta i (dp[i + 1]) o resolverla
#       (puntos + dp[i + poder + 1]).
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            puntos, poder = questions[i]
            siguiente = i + poder + 1
            dp[i] = max(dp[i + 1], puntos + (dp[siguiente] if siguiente < n else 0))
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    assert s.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5
    assert s.mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7
    print("OK")
