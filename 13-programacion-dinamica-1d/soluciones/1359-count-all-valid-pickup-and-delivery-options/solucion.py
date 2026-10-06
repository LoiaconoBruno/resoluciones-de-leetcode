# 1359. Count all Valid Pickup and Delivery Options (Difícil)
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
#
# Idea: si ya tengo un orden válido de i - 1 pedidos (2i - 2 eventos), el pedido nuevo tiene 2i - 1
#       huecos para su recogida y su entrega, con la entrega después: (2i - 1) · 2i / 2 = i · (2i -
#       1) formas. Multiplico para i = 1..n.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 1
        for i in range(2, n + 1):
            res = res * i * (2 * i - 1) % MOD
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.countOrders(1) == 1
    assert s.countOrders(2) == 6
    assert s.countOrders(3) == 90
    print("OK")
