# 658. Find K Closest Elements (Media)
# https://leetcode.com/problems/find-k-closest-elements/
#
# Idea: la respuesta es una ventana de k elementos consecutivos; busco con búsqueda binaria dónde empieza comparando x contra los dos bordes de la ventana.
# Tiempo: O(log(n - k) + k) · Espacio: O(1) extra

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        izq, der = 0, len(arr) - k
        while izq < der:
            medio = (izq + der) // 2
            if x - arr[medio] > arr[medio + k] - x:
                izq = medio + 1
            else:
                der = medio
        return arr[izq:izq + k]


if __name__ == "__main__":
    import random
    s = Solution()
    assert s.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    assert s.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1) == [1, 1, 2, 3]
    assert s.findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    for _ in range(300):
        arr = sorted(random.randint(-10, 10) for _ in range(random.randint(1, 12)))
        k, x = random.randint(1, len(arr)), random.randint(-15, 15)
        esperado = sorted(sorted(arr, key=lambda a: (abs(a - x), a))[:k])
        assert s.findClosestElements(arr, k, x) == esperado
    print("OK")
