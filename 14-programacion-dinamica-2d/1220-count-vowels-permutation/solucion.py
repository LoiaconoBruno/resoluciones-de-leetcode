# 1220. Count Vowels Permutation (Difícil)
# https://leetcode.com/problems/count-vowels-permutation/
#
# Idea: cuento cuántos strings de largo i terminan en cada vocal; para el largo i + 1, cada vocal
#       suma los que terminan en las vocales que la pueden preceder.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = (e + i + u) % MOD, (a + i) % MOD, (e + o) % MOD, i, (i + o) % MOD
        return (a + e + i + o + u) % MOD


if __name__ == "__main__":
    s = Solution()
    assert s.countVowelPermutation(1) == 5
    assert s.countVowelPermutation(2) == 10
    assert s.countVowelPermutation(5) == 68
    print("OK")
