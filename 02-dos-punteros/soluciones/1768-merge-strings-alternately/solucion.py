# 1768. Merge Strings Alternately (Fácil)
# https://leetcode.com/problems/merge-strings-alternately/
#
# Idea: un índice para cada palabra; tomo una letra de cada una por turno y al final pego lo que
#       sobre de la más larga.
# Tiempo: O(n + m) · Espacio: O(n + m)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])
            i += 1
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    assert s.mergeAlternately("abc", "pqr") == "apbqcr"
    assert s.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert s.mergeAlternately("abcd", "pq") == "apbqcd"
    print("OK")
