# 1209. Remove All Adjacent Duplicates In String II (Media)
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
#
# Idea: pila de [letra, cuántas seguidas]; si llega la misma letra sumo uno y, cuando llego a k, saco ese grupo entero.
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        pila = []
        for c in s:
            if pila and pila[-1][0] == c:
                pila[-1][1] += 1
                if pila[-1][1] == k:
                    pila.pop()
            else:
                pila.append([c, 1])
        return "".join(c * veces for c, veces in pila)


if __name__ == "__main__":
    s = Solution()
    assert s.removeDuplicates("abcd", 2) == "abcd"
    assert s.removeDuplicates("deeedbbcccbdaa", 3) == "aa"
    assert s.removeDuplicates("pbbcggttciiippooaais", 2) == "ps"
    print("OK")
