#!/usr/bin/env python3
"""Crea la carpeta de un ejercicio con su README.md y su solucion.py.

Uso: python3 scripts/nuevo.py 217
"""
import sys

from comun import RAIZ, EMOJI, COMANDO_PY, leer_problemas, buscar, carpeta_de, preparar_consola

MARCA_VIDEO = "VIDEO_PENDIENTE"


def completar(texto, problema):
    valores = {
        "{{NUMERO}}": str(int(problema["numero"])),
        "{{TITULO}}": problema["titulo"],
        "{{DIFICULTAD}}": problema["dificultad"],
        "{{EMOJI}}": EMOJI.get(problema["dificultad"], ""),
        "{{PATRON}}": problema["patron"],
        "{{LISTA}}": problema["lista"],
        "{{ENUNCIADO}}": problema["enunciado"],
        "{{VIDEO}}": problema["video"] or MARCA_VIDEO,
    }
    for marca, valor in valores.items():
        texto = texto.replace(marca, valor)
    return texto


def main():
    preparar_consola()
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit(f"Uso: {COMANDO_PY} scripts/nuevo.py NUMERO_DE_LEETCODE   (por ejemplo: 217)")
    problema = buscar(leer_problemas(), int(sys.argv[1]))
    if problema is None:
        sys.exit(f"El problema {sys.argv[1]} no está en problemas.csv.")
    carpeta = carpeta_de(problema)
    rel = carpeta.relative_to(RAIZ).as_posix()
    faltan = [(plantilla, destino)
              for plantilla, destino in (("problema.md", "README.md"), ("solucion.py", "solucion.py"))
              if not (carpeta / destino).exists()]
    if not faltan:
        sys.exit(f"Ya existe {rel}/ con README.md y solucion.py. No toqué nada.")
    carpeta.mkdir(parents=True, exist_ok=True)
    for plantilla, destino in faltan:
        texto = (RAIZ / "plantillas" / plantilla).read_text(encoding="utf-8")
        (carpeta / destino).write_text(completar(texto, problema), encoding="utf-8")
    numero = int(problema["numero"])
    print(f"Listo: {rel}/")
    if ("solucion.py", "solucion.py") in faltan:
        print(f"  1. Escribí la solución en {rel}/solucion.py y probala en LeetCode.")
    else:
        print(f"  1. La solución ya estaba en {rel}/solucion.py: revisala y probala en LeetCode.")
    print(f"  2. Completá {rel}/README.md y guardá el dibujo como {rel}/dibujo.png.")
    print(f"  3. Cuando salga el video: {COMANDO_PY} scripts/publicar.py {numero} URL_DEL_VIDEO")


if __name__ == "__main__":
    main()
