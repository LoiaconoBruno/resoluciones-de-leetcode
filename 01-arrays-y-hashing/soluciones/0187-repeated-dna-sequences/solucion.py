# 187. Repeated DNA Sequences (Media)
# https://leetcode.com/problems/repeated-dna-sequences/
#
# Idea: recorro todas las ventanas de 10 letras guardándolas en un set; si una ya estaba, va a la
#       respuesta.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        vistas, repetidas = set(), set()
        for i in range(len(s) - 9):
            ventana = s[i:i + 10]
            if ventana in vistas:
                repetidas.add(ventana)
            vistas.add(ventana)
        return list(repetidas)


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) == ["AAAAACCCCC", "CCCCCAAAAA"]
    assert s.findRepeatedDnaSequences("AAAAAAAAAAAAA") == ["AAAAAAAAAA"]
    print("OK")
