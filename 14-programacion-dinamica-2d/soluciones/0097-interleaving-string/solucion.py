# 97. Interleaving String (Media)
# https://leetcode.com/problems/interleaving-string/
#
# Idea: dp[i][j] dice si con los primeros i de s1 y los primeros j de s2 armo los primeros i + j de
#       s3; la última letra vino de s1 o de s2.
# Tiempo: O(n · m) · Espacio: O(m)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2) + 1)
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == j == 0:
                    dp[j] = True
                    continue
                desde_s1 = i > 0 and dp[j] and s1[i - 1] == s3[i + j - 1]
                desde_s2 = j > 0 and dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[j] = desde_s1 or desde_s2
        return dp[len(s2)]


if __name__ == "__main__":
    s = Solution()
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
    assert s.isInterleave("", "", "") is True
    print("OK")
