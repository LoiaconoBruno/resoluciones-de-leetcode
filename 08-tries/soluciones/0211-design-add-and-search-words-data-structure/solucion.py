# 211. Design Add And Search Words Data Structure (Media)
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
#
# Idea: un trie normal; al buscar, un '.' prueba con todos los hijos del nodo actual (DFS), y una
#       letra común baja por un solo camino.
# Tiempo: O(m) addWord; search O(26^p · m) en el peor caso, con p la cantidad de puntos · Espacio: O(total de letras)

class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.fin = False


class WordDictionary:
    def __init__(self):
        self.raiz = NodoTrie()

    def addWord(self, word: str) -> None:
        nodo = self.raiz
        for c in word:
            nodo = nodo.hijos.setdefault(c, NodoTrie())
        nodo.fin = True

    def search(self, word: str) -> bool:
        def buscar(nodo, i):
            if i == len(word):
                return nodo.fin
            c = word[i]
            if c == ".":
                return any(buscar(hijo, i + 1) for hijo in nodo.hijos.values())
            return c in nodo.hijos and buscar(nodo.hijos[c], i + 1)

        return buscar(self.raiz, 0)


if __name__ == "__main__":
    d = WordDictionary()
    for p in ("bad", "dad", "mad"):
        d.addWord(p)
    assert d.search("pad") is False
    assert d.search("bad") is True
    assert d.search(".ad") is True
    assert d.search("b..") is True
    assert d.search("b...") is False
    print("OK")
