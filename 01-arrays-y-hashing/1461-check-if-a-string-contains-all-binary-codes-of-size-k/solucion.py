# 1461. Check if a String Contains all Binary Codes of Size K (Media)
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
#
# Idea: guardo en un set todas las ventanas de largo k; hay 2^k códigos posibles, así que alcanza con comparar la cantidad.
# Tiempo: O(n · k) · Espacio: O(n · k)

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        vistos = {s[i:i + k] for i in range(len(s) - k + 1)}
        return len(vistos) == 1 << k


if __name__ == "__main__":
    s = Solution()
    assert s.hasAllCodes("00110110", 2) is True
    assert s.hasAllCodes("0110", 1) is True
    assert s.hasAllCodes("0110", 2) is False
    print("OK")
