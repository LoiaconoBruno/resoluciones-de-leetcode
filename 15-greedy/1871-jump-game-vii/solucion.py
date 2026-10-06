# 1871. Jump Game VII (Media)
# https://leetcode.com/problems/jump-game-vii/
#
# Idea: a la posición i (con '0') llego si alguna posición alcanzable está en [i - maxJump, i -
#       minJump]. Llevo cuántas alcanzables hay en esa ventana y la deslizo sumando la que entra y
#       restando la que sale.
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        alcanzable = [False] * n
        alcanzable[0] = True
        en_ventana = 0
        for i in range(1, n):
            if i >= minJump and alcanzable[i - minJump]:
                en_ventana += 1
            if i > maxJump and alcanzable[i - maxJump - 1]:
                en_ventana -= 1
            alcanzable[i] = en_ventana > 0 and s[i] == "0"
        return alcanzable[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.canReach("011010", 2, 3) is True
    assert s.canReach("01101110", 2, 3) is False
    print("OK")
