# 68. Text Justification (Difícil)
# https://leetcode.com/problems/text-justification/
#
# Idea: meto palabras en la línea mientras entren; al cerrarla reparto los espacios sobrantes entre
#       los huecos (los de la izquierda reciben uno más). La última línea va alineada a la
#       izquierda.
# Tiempo: O(total de caracteres) · Espacio: O(maxWidth) extra

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        linea, letras = [], 0
        for palabra in words:
            if letras + len(palabra) + len(linea) > maxWidth:
                espacios = maxWidth - letras
                huecos = len(linea) - 1
                if huecos == 0:
                    res.append(linea[0] + " " * espacios)
                else:
                    base, extra = divmod(espacios, huecos)
                    texto = ""
                    for j, p in enumerate(linea[:-1]):
                        texto += p + " " * (base + (1 if j < extra else 0))
                    res.append(texto + linea[-1])
                linea, letras = [], 0
            linea.append(palabra)
            letras += len(palabra)
        ultima = " ".join(linea)
        res.append(ultima + " " * (maxWidth - len(ultima)))
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == \
        ["This    is    an", "example  of text", "justification.  "]
    assert s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16) == \
        ["What   must   be", "acknowledgment  ", "shall be        "]
    assert s.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                          "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20) == \
        ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is",
         "everything  else  we", "do                  "]
    print("OK")
