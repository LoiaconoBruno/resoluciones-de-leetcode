# 96. Unique Binary Search Trees (Media)
# https://leetcode.com/problems/unique-binary-search-trees/
#
# Idea: si la raíz es i, a la izquierda quedan i - 1 nodos y a la derecha n - i; las formas se
#       multiplican. arboles[n] = suma de arboles[i - 1] · arboles[n - i] (números de Catalan).
# Tiempo: O(n²) · Espacio: O(n)

class Solution:
    def numTrees(self, n: int) -> int:
        arboles = [1] * (n + 1)
        for nodos in range(2, n + 1):
            arboles[nodos] = sum(arboles[raiz - 1] * arboles[nodos - raiz] for raiz in range(1, nodos + 1))
        return arboles[n]


if __name__ == "__main__":
    s = Solution()
    assert s.numTrees(3) == 5
    assert s.numTrees(1) == 1
    assert s.numTrees(19) == 1767263190
    print("OK")
