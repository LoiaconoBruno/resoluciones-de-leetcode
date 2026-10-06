# 535. Encode and Decode TinyURL (Media)
# https://leetcode.com/problems/encode-and-decode-tinyurl/
#
# Idea: a cada URL larga le doy un número correlativo como código corto y guardo las dos direcciones en diccionarios.
# Tiempo: O(1) por operación (sin contar el largo de la URL) · Espacio: O(n)

class Codec:
    BASE = "http://tinyurl.com/"

    def __init__(self):
        self.corta_a_larga = {}
        self.larga_a_corta = {}

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.larga_a_corta:
            corta = self.BASE + str(len(self.corta_a_larga) + 1)
            self.larga_a_corta[longUrl] = corta
            self.corta_a_larga[corta] = longUrl
        return self.larga_a_corta[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.corta_a_larga[shortUrl]


if __name__ == "__main__":
    c = Codec()
    for url in ("https://leetcode.com/problems/design-tinyurl", "https://example.com", "https://leetcode.com/problems/design-tinyurl"):
        assert c.decode(c.encode(url)) == url
    print("OK")
