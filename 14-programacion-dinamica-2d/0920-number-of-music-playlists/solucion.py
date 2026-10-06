# 920. Number of Music Playlists (Difícil)
# https://leetcode.com/problems/number-of-music-playlists/
#
# Idea: dp[i][j] = playlists de i canciones con j canciones distintas. La i-ésima es nueva (n - (j -
#       1) opciones) o repetida, y solo puedo repetir alguna de las j - k que no sonaron en las
#       últimas k.
# Tiempo: O(goal · n) · Espacio: O(goal · n)

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                nueva = dp[i - 1][j - 1] * (n - j + 1)
                repetida = dp[i - 1][j] * max(j - k, 0)
                dp[i][j] = (nueva + repetida) % MOD
        return dp[goal][n]


if __name__ == "__main__":
    s = Solution()
    assert s.numMusicPlaylists(3, 3, 1) == 6
    assert s.numMusicPlaylists(2, 3, 0) == 6
    assert s.numMusicPlaylists(2, 3, 1) == 2
    print("OK")
