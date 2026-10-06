# 297. Serialize And Deserialize Binary Tree (Difícil)
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#
# Idea: serializo en preorden escribiendo "N" para cada hueco; al deserializar leo los valores en el
#       mismo orden y reconstruyo con la misma recursión.
# Tiempo: O(n) · Espacio: O(n)

# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        partes = []

        def recorrer(nodo):
            if not nodo:
                partes.append("N")
                return
            partes.append(str(nodo.val))
            recorrer(nodo.left)
            recorrer(nodo.right)

        recorrer(root)
        return ",".join(partes)

    def deserialize(self, data):
        valores = iter(data.split(","))

        def armar():
            v = next(valores)
            if v == "N":
                return None
            nodo = TreeNode(int(v))
            nodo.left = armar()
            nodo.right = armar()
            return nodo

        return armar()


if __name__ == "__main__":
    def crear(valores):
        # Arma el árbol desde la lista por niveles que usa LeetCode (None = hueco).
        if not valores or valores[0] is None:
            return None
        raiz = TreeNode(valores[0])
        pendientes = [raiz]
        i = 1
        for nodo in pendientes:
            for lado in ("left", "right"):
                if i < len(valores) and valores[i] is not None:
                    hijo = TreeNode(valores[i])
                    setattr(nodo, lado, hijo)
                    pendientes.append(hijo)
                i += 1
        return raiz

    def a_lista(raiz):
        # El camino inverso: árbol -> lista por niveles, sin los None del final.
        res, nodos = [], [raiz]
        for nodo in nodos:
            if nodo:
                res.append(nodo.val)
                nodos += [nodo.left, nodo.right]
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        return res

    c = Codec()
    for valores in ([1, 2, 3, None, None, 4, 5], [], [-1, None, -2], [5, 4, 7, 3, None, 2, None, -1, None, 9]):
        assert a_lista(c.deserialize(c.serialize(crear(valores)))) == valores
    print("OK")
