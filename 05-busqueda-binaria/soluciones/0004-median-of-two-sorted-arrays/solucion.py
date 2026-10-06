# 4. Median of Two Sorted Arrays (Difícil)
# https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# Idea: hago búsqueda binaria sobre cuántos elementos tomo del array más corto para la "mitad
#       izquierda"; el corte es correcto cuando todo lo de la izquierda es ≤ todo lo de la derecha.
# Tiempo: O(log(min(n, m))) · Espacio: O(1)

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a
        total = len(a) + len(b)
        mitad = (total + 1) // 2
        izq, der = 0, len(a)
        infinito = float("inf")
        while True:
            i = (izq + der) // 2
            j = mitad - i
            a_izq = a[i - 1] if i > 0 else -infinito
            a_der = a[i] if i < len(a) else infinito
            b_izq = b[j - 1] if j > 0 else -infinito
            b_der = b[j] if j < len(b) else infinito
            if a_izq <= b_der and b_izq <= a_der:
                if total % 2:
                    return float(max(a_izq, b_izq))
                return (max(a_izq, b_izq) + min(a_der, b_der)) / 2
            if a_izq > b_der:
                der = i - 1
            else:
                izq = i + 1


if __name__ == "__main__":
    import random
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    for _ in range(500):
        a = sorted(random.randint(-20, 20) for _ in range(random.randint(0, 8)))
        b = sorted(random.randint(-20, 20) for _ in range(random.randint(0 if a else 1, 8)))
        todo = sorted(a + b)
        n = len(todo)
        esperado = todo[n // 2] if n % 2 else (todo[n // 2 - 1] + todo[n // 2]) / 2
        assert s.findMedianSortedArrays(a, b) == esperado
    print("OK")
