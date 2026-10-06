# 67. Add Binary (Fácil)
# https://leetcode.com/problems/add-binary/
#
# Idea: sumo de derecha a izquierda bit por bit con acarreo, como una suma en papel pero en base 2.
# Tiempo: O(max(n, m)) · Espacio: O(max(n, m))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        acarreo = 0
        while i >= 0 or j >= 0 or acarreo:
            total = acarreo
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            acarreo, bit = divmod(total, 2)
            res.append(str(bit))
        return "".join(reversed(res))


if __name__ == "__main__":
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
    assert s.addBinary("0", "0") == "0"
    print("OK")
