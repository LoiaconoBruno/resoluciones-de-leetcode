# 1041. Robot Bounded In Circle (Media)
# https://leetcode.com/problems/robot-bounded-in-circle/
#
# Idea: simulo las instrucciones una vez. Si el robot volvió al origen, o si no mira al norte, en a
#       lo sumo 4 repeticiones vuelve al inicio: queda encerrado en un círculo.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        dx, dy = 0, 1
        for c in instructions:
            if c == "G":
                x, y = x + dx, y + dy
            elif c == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)


if __name__ == "__main__":
    s = Solution()
    assert s.isRobotBounded("GGLLGG") is True
    assert s.isRobotBounded("GG") is False
    assert s.isRobotBounded("GL") is True
    print("OK")
