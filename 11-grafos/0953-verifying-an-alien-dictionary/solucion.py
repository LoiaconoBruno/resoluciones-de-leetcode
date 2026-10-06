# 953. Verifying An Alien Dictionary (Fácil)
# https://leetcode.com/problems/verifying-an-alien-dictionary/
#
# Idea: alcanza con comparar cada palabra con la siguiente: busco la primera letra distinta y
#       verifico que estén en el orden del alfabeto alienígena. Si no hay diferencia, la más corta
#       tiene que ir primero.
# Tiempo: O(total de letras) · Espacio: O(1) (26 letras)

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        posicion = {letra: i for i, letra in enumerate(order)}
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if posicion[x] > posicion[y]:
                        return False
                    break
            else:
                if len(a) > len(b):
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") is True
    assert s.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") is False
    assert s.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") is False
    print("OK")
