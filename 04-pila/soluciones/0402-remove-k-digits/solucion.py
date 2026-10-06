# 402. Remove K Digits (Media)
# https://leetcode.com/problems/remove-k-digits/
#
# Idea: pila creciente: si el dígito que llega es menor que el de arriba, sacar el de arriba achica
#       el número (todavía puedo borrar k). Al final saco lo que sobre del final y los ceros de
#       adelante.
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        pila = []
        for d in num:
            while k and pila and pila[-1] > d:
                pila.pop()
                k -= 1
            pila.append(d)
        if k:
            pila = pila[:-k]
        return "".join(pila).lstrip("0") or "0"


if __name__ == "__main__":
    s = Solution()
    assert s.removeKdigits("1432219", 3) == "1219"
    assert s.removeKdigits("10200", 1) == "200"
    assert s.removeKdigits("10", 2) == "0"
    assert s.removeKdigits("112", 1) == "11"
    print("OK")
