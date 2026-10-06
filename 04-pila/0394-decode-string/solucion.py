# 394. Decode String (Media)
# https://leetcode.com/problems/decode-string/
#
# Idea: al abrir '[' guardo en la pila lo armado hasta ahí y el número de repeticiones; al cerrar ']' repito lo de adentro y lo pego a lo que había guardado.
# Tiempo: O(largo de la respuesta) · Espacio: O(largo de la respuesta)

class Solution:
    def decodeString(self, s: str) -> str:
        pila = []
        actual = ""
        numero = 0
        for c in s:
            if c.isdigit():
                numero = numero * 10 + int(c)
            elif c == "[":
                pila.append((actual, numero))
                actual, numero = "", 0
            elif c == "]":
                anterior, veces = pila.pop()
                actual = anterior + actual * veces
            else:
                actual += c
        return actual


if __name__ == "__main__":
    s = Solution()
    assert s.decodeString("3[a]2[bc]") == "aaabcbc"
    assert s.decodeString("3[a2[c]]") == "accaccacc"
    assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert s.decodeString("10[a]") == "aaaaaaaaaa"
    print("OK")
