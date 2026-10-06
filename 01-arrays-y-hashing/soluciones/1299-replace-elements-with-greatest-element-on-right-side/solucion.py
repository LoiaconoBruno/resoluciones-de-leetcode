# 1299. Replace Elements With Greatest Element On Right Side (Fácil)
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
#
# Idea: recorro de derecha a izquierda llevando el máximo visto; cada posición se queda con el
#       máximo de lo que tenía a su derecha.
# Tiempo: O(n) · Espacio: O(1) extra

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximo = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], maximo = maximo, max(maximo, arr[i])
        return arr


if __name__ == "__main__":
    s = Solution()
    assert s.replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
    assert s.replaceElements([400]) == [-1]
    print("OK")
