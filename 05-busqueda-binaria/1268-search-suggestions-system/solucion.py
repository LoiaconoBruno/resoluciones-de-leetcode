# 1268. Search Suggestions System (Media)
# https://leetcode.com/problems/search-suggestions-system/
#
# Idea: ordeno los productos; para cada prefijo, búsqueda binaria de la primera palabra ≥ prefijo y tomo hasta 3 desde ahí que empiecen con ese prefijo.
# Tiempo: O(n log n + m · log n), con m el largo de searchWord · Espacio: O(1) extra (sin contar la respuesta)

from bisect import bisect_left
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefijo = ""
        for c in searchWord:
            prefijo += c
            i = bisect_left(products, prefijo)
            res.append([p for p in products[i:i + 3] if p.startswith(prefijo)])
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse") == [
        ["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
    assert s.suggestedProducts(["havana"], "havana") == [["havana"]] * 6
    assert s.suggestedProducts(["havana"], "tatiana") == [[]] * 7
    print("OK")
