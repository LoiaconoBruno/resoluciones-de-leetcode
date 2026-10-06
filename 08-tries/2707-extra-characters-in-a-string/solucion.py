# 2707. Extra Characters in a String (Media)
# https://leetcode.com/problems/extra-characters-in-a-string/
#
# Idea: dp[i] = mínimo de caracteres sobrantes en s[i:]. Desde i, o el carácter sobra (1 + dp[i +
#       1]) o bajo por un trie del diccionario y, por cada palabra que termina en j, pruebo dp[j +
#       1].
# Tiempo: O(n² + total del diccionario) · Espacio: O(n + total del diccionario)

from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        raiz = {}
        for palabra in dictionary:
            nodo = raiz
            for c in palabra:
                nodo = nodo.setdefault(c, {})
            nodo["$"] = True

        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            nodo = raiz
            for j in range(i, n):
                if s[j] not in nodo:
                    break
                nodo = nodo[s[j]]
                if "$" in nodo:
                    dp[i] = min(dp[i], dp[j + 1])
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    assert s.minExtraChar("leetscode", ["leet", "code", "leetcode"]) == 1
    assert s.minExtraChar("sayhelloworld", ["hello", "world"]) == 3
    print("OK")
