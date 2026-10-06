# 93. Restore IP Addresses (Media)
# https://leetcode.com/problems/restore-ip-addresses/
#
# Idea: armo 4 partes; cada parte toma 1, 2 o 3 dígitos y es válida si está entre 0 y 255 y no tiene
#       ceros adelante (salvo el "0" solo).
# Tiempo: O(3^4 · n) = O(1), porque el largo está acotado · Espacio: O(1)

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        partes = []

        def armar(i):
            if len(partes) == 4:
                if i == len(s):
                    res.append(".".join(partes))
                return
            for largo in range(1, 4):
                parte = s[i:i + largo]
                if len(parte) < largo or (parte[0] == "0" and largo > 1) or int(parte) > 255:
                    break
                partes.append(parte)
                armar(i + largo)
                partes.pop()

        armar(0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.restoreIpAddresses("25525511135")) == ["255.255.11.135", "255.255.111.35"]
    assert s.restoreIpAddresses("0000") == ["0.0.0.0"]
    assert sorted(s.restoreIpAddresses("101023")) == \
        ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    print("OK")
