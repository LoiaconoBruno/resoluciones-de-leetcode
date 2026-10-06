# 1189. Maximum Number of Balloons (Fácil)
# https://leetcode.com/problems/maximum-number-of-balloons/
#
# Idea: cuento las letras del texto y veo cuántas veces me alcanza cada letra de "balloon" (la 'l' y
#       la 'o' se usan dos veces); el mínimo manda.
# Tiempo: O(n) · Espacio: O(1)

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        tengo = Counter(text)
        necesito = Counter("balloon")
        return min(tengo[c] // necesito[c] for c in necesito)


if __name__ == "__main__":
    s = Solution()
    assert s.maxNumberOfBalloons("nlaebolko") == 1
    assert s.maxNumberOfBalloons("loonbalxballpoon") == 2
    assert s.maxNumberOfBalloons("leetcode") == 0
    print("OK")
