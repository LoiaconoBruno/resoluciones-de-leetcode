# 71. Simplify Path (Media)
# https://leetcode.com/problems/simplify-path/
#
# Idea: separo por '/' y uso una pila de carpetas: '..' saca la última, '.' y vacío no hacen nada, y
#       cualquier otro nombre se apila.
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def simplifyPath(self, path: str) -> str:
        pila = []
        for parte in path.split("/"):
            if parte == "..":
                if pila:
                    pila.pop()
            elif parte and parte != ".":
                pila.append(parte)
        return "/" + "/".join(pila)


if __name__ == "__main__":
    s = Solution()
    assert s.simplifyPath("/home/") == "/home"
    assert s.simplifyPath("/home//foo/") == "/home/foo"
    assert s.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"
    assert s.simplifyPath("/../") == "/"
    assert s.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"
    print("OK")
