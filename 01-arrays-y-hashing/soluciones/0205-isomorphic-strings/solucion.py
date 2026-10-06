# 205. Isomorphic Strings (Fácil)
# https://leetcode.com/problems/isomorphic-strings/
#
# Idea: armo dos diccionarios (s -> t y t -> s); si alguna letra ya estaba asignada a otra distinta,
#       no son isomorfos.
# Tiempo: O(n) · Espacio: O(1) (el alfabeto es acotado)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_a_t, t_a_s = {}, {}
        for a, b in zip(s, t):
            if s_a_t.get(a, b) != b or t_a_s.get(b, a) != a:
                return False
            s_a_t[a] = b
            t_a_s[b] = a
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isIsomorphic("egg", "add") is True
    assert s.isIsomorphic("foo", "bar") is False
    assert s.isIsomorphic("paper", "title") is True
    assert s.isIsomorphic("badc", "baba") is False
    print("OK")
