# 1647. Minimum Deletions to Make Character Frequencies Unique (Media)
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
#
# Idea: recorro las frecuencias de mayor a menor; cada una tiene que quedar estrictamente debajo de
#       la anterior que dejé (o en 0), así que borro lo justo para que entre.
# Tiempo: O(n + 26 log 26) · Espacio: O(1)

from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        borrados = 0
        tope = float("inf")
        for f in sorted(Counter(s).values(), reverse=True):
            permitido = max(min(f, tope), 0)
            borrados += f - permitido
            tope = permitido - 1
        return borrados


if __name__ == "__main__":
    s = Solution()
    assert s.minDeletions("aab") == 0
    assert s.minDeletions("aaabbbcc") == 2
    assert s.minDeletions("ceabaacb") == 2
    print("OK")
