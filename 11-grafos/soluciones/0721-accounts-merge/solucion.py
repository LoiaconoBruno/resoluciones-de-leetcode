# 721. Accounts Merge (Media)
# https://leetcode.com/problems/accounts-merge/
#
# Idea: union-find sobre las cuentas: si un mail ya apareció en otra cuenta, uno las dos. Al final
#       agrupo los mails por la raíz de su cuenta, los ordeno y les pongo el nombre.
# Tiempo: O(N log N), con N el total de mails · Espacio: O(N)

from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        padre = list(range(len(accounts)))

        def raiz(x):
            while padre[x] != x:
                padre[x] = padre[padre[x]]
                x = padre[x]
            return x

        duenio = {}
        for i, cuenta in enumerate(accounts):
            for mail in cuenta[1:]:
                if mail in duenio:
                    padre[raiz(i)] = raiz(duenio[mail])
                else:
                    duenio[mail] = i
        grupos = defaultdict(list)
        for mail, i in duenio.items():
            grupos[raiz(i)].append(mail)
        return [[accounts[i][0]] + sorted(mails) for i, mails in grupos.items()]


if __name__ == "__main__":
    s = Solution()
    cuentas = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
               ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
    assert sorted(s.accountsMerge(cuentas)) == sorted([
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
    cuentas = [["A", "a@x", "b@x"], ["A", "c@x"], ["A", "c@x", "b@x"]]
    assert s.accountsMerge(cuentas) == [["A", "a@x", "b@x", "c@x"]]
    print("OK")
