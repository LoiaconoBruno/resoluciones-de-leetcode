# 2390. Removing Stars From a String (Media)
# https://leetcode.com/problems/removing-stars-from-a-string/
#
# Idea: apilo las letras y cada estrella saca la última apilada, que es justo la letra más cercana a su izquierda.
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def removeStars(self, s: str) -> str:
        pila = []
        for c in s:
            if c == "*":
                pila.pop()
            else:
                pila.append(c)
        return "".join(pila)


if __name__ == "__main__":
    s = Solution()
    assert s.removeStars("leet**cod*e") == "lecoe"
    assert s.removeStars("erase*****") == ""
    print("OK")
