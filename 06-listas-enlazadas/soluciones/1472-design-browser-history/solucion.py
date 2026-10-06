# 1472. Design Browser History (Media)
# https://leetcode.com/problems/design-browser-history/
#
# Idea: guardo el historial en un array con un índice "actual" y un "último válido"; visit pisa lo
#       que había adelante, y back/forward solo mueven el índice dentro de los límites.
# Tiempo: O(1) por operación (amortizado en visit) · Espacio: O(n)

class BrowserHistory:
    def __init__(self, homepage: str):
        self.paginas = [homepage]
        self.actual = 0
        self.ultimo = 0

    def visit(self, url: str) -> None:
        self.actual += 1
        if self.actual == len(self.paginas):
            self.paginas.append(url)
        else:
            self.paginas[self.actual] = url
        self.ultimo = self.actual

    def back(self, steps: int) -> str:
        self.actual = max(0, self.actual - steps)
        return self.paginas[self.actual]

    def forward(self, steps: int) -> str:
        self.actual = min(self.ultimo, self.actual + steps)
        return self.paginas[self.actual]


if __name__ == "__main__":
    b = BrowserHistory("leetcode.com")
    b.visit("google.com")
    b.visit("facebook.com")
    b.visit("youtube.com")
    assert b.back(1) == "facebook.com"
    assert b.back(1) == "google.com"
    assert b.forward(1) == "facebook.com"
    b.visit("linkedin.com")
    assert b.forward(2) == "linkedin.com"
    assert b.back(2) == "google.com"
    assert b.back(7) == "leetcode.com"
    print("OK")
