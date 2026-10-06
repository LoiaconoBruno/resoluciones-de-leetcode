# 735. Asteroid Collision (Media)
# https://leetcode.com/problems/asteroid-collision/
#
# Idea: solo chocan un asteroide que va a la derecha (en la pila) con uno que llega yendo a la izquierda; resuelvo los choques contra el tope de la pila hasta que el nuevo explota o pasa.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pila = []
        for a in asteroids:
            vivo = True
            while vivo and a < 0 and pila and pila[-1] > 0:
                if pila[-1] < -a:
                    pila.pop()
                elif pila[-1] == -a:
                    pila.pop()
                    vivo = False
                else:
                    vivo = False
            if vivo:
                pila.append(a)
        return pila


if __name__ == "__main__":
    s = Solution()
    assert s.asteroidCollision([5, 10, -5]) == [5, 10]
    assert s.asteroidCollision([8, -8]) == []
    assert s.asteroidCollision([10, 2, -5]) == [10]
    assert s.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    print("OK")
