# 108. Convert Sorted Array to Binary Search Tree (Fácil)
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#
# Idea: el del medio es la raíz (así quedan mitades del mismo tamaño); la mitad izquierda arma el
#       subárbol izquierdo y la derecha el derecho.
# Tiempo: O(n) · Espacio: O(log n) de recursión

from typing import List, Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def armar(izq, der):
            if izq > der:
                return None
            medio = (izq + der) // 2
            return TreeNode(nums[medio], armar(izq, medio - 1), armar(medio + 1, der))

        return armar(0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution()

    def inorden(n):
        return inorden(n.left) + [n.val] + inorden(n.right) if n else []

    def altura_si_balanceado(n):
        if not n:
            return 0
        i, d = altura_si_balanceado(n.left), altura_si_balanceado(n.right)
        assert abs(i - d) <= 1
        return 1 + max(i, d)

    for nums in ([-10, -3, 0, 5, 9], [1, 3], list(range(20))):
        raiz = s.sortedArrayToBST(nums)
        assert inorden(raiz) == nums
        altura_si_balanceado(raiz)
    print("OK")
