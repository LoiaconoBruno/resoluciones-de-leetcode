# 290. Word Pattern (Fácil)
# https://leetcode.com/problems/word-pattern/
#
# Idea: es el mismo problema que strings isomorfos, pero letra contra palabra: dos diccionarios para
#       que la relación sea uno a uno.
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        palabras = s.split()
        if len(palabras) != len(pattern):
            return False
        letra_a_palabra, palabra_a_letra = {}, {}
        for letra, palabra in zip(pattern, palabras):
            if letra_a_palabra.get(letra, palabra) != palabra:
                return False
            if palabra_a_letra.get(palabra, letra) != letra:
                return False
            letra_a_palabra[letra] = palabra
            palabra_a_letra[palabra] = letra
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.wordPattern("abba", "dog cat cat dog") is True
    assert s.wordPattern("abba", "dog cat cat fish") is False
    assert s.wordPattern("aaaa", "dog cat cat dog") is False
    assert s.wordPattern("abba", "dog dog dog dog") is False
    assert s.wordPattern("aaa", "aa aa aa aa") is False
    print("OK")
