# 208. Implement Trie Prefix Tree (Media)
# https://leetcode.com/problems/implement-trie-prefix-tree/
#
# Idea: cada nodo tiene un diccionario letra -> hijo y una marca de "acá termina una palabra";
#       insertar y buscar es bajar letra por letra.
# Tiempo: O(largo de la palabra) por operación · Espacio: O(total de letras insertadas)

class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.fin = False


class Trie:
    def __init__(self):
        self.raiz = NodoTrie()

    def insert(self, word: str) -> None:
        nodo = self.raiz
        for c in word:
            nodo = nodo.hijos.setdefault(c, NodoTrie())
        nodo.fin = True

    def _bajar(self, texto):
        nodo = self.raiz
        for c in texto:
            if c not in nodo.hijos:
                return None
            nodo = nodo.hijos[c]
        return nodo

    def search(self, word: str) -> bool:
        nodo = self._bajar(word)
        return nodo is not None and nodo.fin

    def startsWith(self, prefix: str) -> bool:
        return self._bajar(prefix) is not None


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.startsWith("app") is True
    t.insert("app")
    assert t.search("app") is True
    assert t.startsWith("b") is False
    print("OK")
