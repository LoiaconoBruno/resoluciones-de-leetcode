# 763. Partition Labels (Media)
# https://leetcode.com/problems/partition-labels/
#
# Idea: guardo la última aparición de cada letra; voy extendiendo el final de la parte actual hasta
#       la última aparición de cada letra que veo, y corto cuando llego a ese final.
# Tiempo: O(n) · Espacio: O(1) (26 letras)

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ultima = {c: i for i, c in enumerate(s)}
        res = []
        inicio = fin = 0
        for i, c in enumerate(s):
            fin = max(fin, ultima[c])
            if i == fin:
                res.append(fin - inicio + 1)
                inicio = i + 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert s.partitionLabels("eccbbbbdec") == [10]
    print("OK")
