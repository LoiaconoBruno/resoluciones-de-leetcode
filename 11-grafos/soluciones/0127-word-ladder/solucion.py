# 127. Word Ladder (Difícil)
# https://leetcode.com/problems/word-ladder/
#
# Idea: BFS donde cada palabra es un nodo. Para encontrar vecinos rápido, agrupo las palabras por
#       patrón con un comodín ("h*t" agrupa hot, hit...): dos palabras son vecinas si comparten
#       patrón.
# Tiempo: O(n · m²), con m el largo de las palabras · Espacio: O(n · m²)

from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patrones = defaultdict(list)
        for palabra in wordList + [beginWord]:
            for i in range(len(palabra)):
                patrones[palabra[:i] + "*" + palabra[i + 1:]].append(palabra)
        vistas = {beginWord}
        cola = deque([beginWord])
        pasos = 1
        while cola:
            for _ in range(len(cola)):
                palabra = cola.popleft()
                if palabra == endWord:
                    return pasos
                for i in range(len(palabra)):
                    patron = palabra[:i] + "*" + palabra[i + 1:]
                    for vecina in patrones[patron]:
                        if vecina not in vistas:
                            vistas.add(vecina)
                            cola.append(vecina)
                    patrones[patron] = []
            pasos += 1
        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    print("OK")
