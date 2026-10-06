# 271. Encode and Decode Strings (Media)
# https://www.lintcode.com/problem/659/
#
# Idea: antes de cada palabra escribo su largo y un '#'; al decodificar leo el número hasta el '#' y
#       sé exactamente cuántos caracteres tomar, aunque la palabra tenga '#'.
# Tiempo: O(n), con n el total de caracteres · Espacio: O(n)

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(p)}#{p}" for p in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            largo = int(s[i:j])
            res.append(s[j + 1:j + 1 + largo])
            i = j + 1 + largo
        return res


if __name__ == "__main__":
    s = Solution()
    for caso in (["lint", "code", "love", "you"], ["we", "say", ":", "yes"], [""], [], ["a#b", "##", "12#"]):
        assert s.decode(s.encode(caso)) == caso
    print("OK")
