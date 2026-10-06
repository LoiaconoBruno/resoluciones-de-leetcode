# 1963. Minimum Number of Swaps to Make The String Balanced (Media)
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
#
# Idea: tacho los pares [] que ya cierran bien; quedan m corchetes ']' sin pareja y cada intercambio
#       arregla dos, así que la respuesta es (m + 1) // 2.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def minSwaps(self, s: str) -> int:
        abiertos = sin_pareja = 0
        for c in s:
            if c == "[":
                abiertos += 1
            elif abiertos:
                abiertos -= 1
            else:
                sin_pareja += 1
        return (sin_pareja + 1) // 2


if __name__ == "__main__":
    s = Solution()
    assert s.minSwaps("][][") == 1
    assert s.minSwaps("]]][[[") == 2
    assert s.minSwaps("[]") == 0
    print("OK")
