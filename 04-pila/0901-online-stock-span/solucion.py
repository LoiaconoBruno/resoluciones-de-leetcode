# 901. Online Stock Span (Media)
# https://leetcode.com/problems/online-stock-span/
#
# Idea: pila de (precio, span) decreciente; un precio nuevo se "come" a todos los menores o iguales de la pila sumando sus spans.
# Tiempo: O(1) amortizado por llamada · Espacio: O(n)

class StockSpanner:
    def __init__(self):
        self.pila = []

    def next(self, price: int) -> int:
        span = 1
        while self.pila and self.pila[-1][0] <= price:
            span += self.pila.pop()[1]
        self.pila.append((price, span))
        return span


if __name__ == "__main__":
    st = StockSpanner()
    assert [st.next(p) for p in [100, 80, 60, 70, 60, 75, 85]] == [1, 1, 1, 2, 1, 4, 6]
    print("OK")
