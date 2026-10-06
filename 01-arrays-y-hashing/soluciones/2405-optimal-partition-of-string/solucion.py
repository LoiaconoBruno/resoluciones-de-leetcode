# 2405. Optimal Partition of String (Media)
# https://leetcode.com/problems/optimal-partition-of-string/
#
# Idea: greedy: estiro la parte actual lo más posible y corto recién cuando aparece una letra
#       repetida.
# Tiempo: O(n) · Espacio: O(1) (26 letras)

class Solution:
    def partitionString(self, s: str) -> int:
        partes = 1
        actual = set()
        for c in s:
            if c in actual:
                partes += 1
                actual.clear()
            actual.add(c)
        return partes


if __name__ == "__main__":
    s = Solution()
    assert s.partitionString("abacaba") == 4
    assert s.partitionString("ssssss") == 6
    print("OK")
