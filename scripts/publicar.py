#!/usr/bin/env python3
"""Marca un ejercicio como publicado, actualiza el índice y hace el commit.

Uso: python3 scripts/publicar.py 217 https://youtube.com/shorts/xxxx
     python3 scripts/publicar.py 217 https://youtube.com/shorts/xxxx --sin-commit
"""
import subprocess
import sys

import generar_indice
from comun import (RAIZ, COMANDO_PY, leer_problemas, guardar_problemas, buscar, carpeta_de,
                   preparar_consola)

MARCA_SOLUCION = "TODO: tu solución"
MARCA_VIDEO = "VIDEO_PENDIENTE"


def git(*args):
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True)


def main():
    preparar_consola()
    opciones = [a for a in sys.argv[1:] if a.startswith("--")]
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args or not args[0].isdigit() or len(args) > 2 or set(opciones) - {"--sin-commit"}:
        sys.exit(f"Uso: {COMANDO_PY} scripts/publicar.py NUMERO [URL_DEL_VIDEO] [--sin-commit]")
    numero = int(args[0])
    url = args[1] if len(args) == 2 else ""

    problemas = leer_problemas()
    problema = buscar(problemas, numero)
    if problema is None:
        sys.exit(f"El problema {numero} no está en problemas.csv.")
    carpeta = carpeta_de(problema)
    rel = carpeta.relative_to(RAIZ).as_posix()
    solucion = carpeta / "solucion.py"
    if not solucion.exists() or not (carpeta / "README.md").exists():
        sys.exit(f"Primero completá la carpeta: {COMANDO_PY} scripts/nuevo.py {numero}")
    if MARCA_SOLUCION in solucion.read_text(encoding="utf-8"):
        sys.exit(f"{rel}/solucion.py todavía es la plantilla. Pegá tu solución antes de publicar.")
    if not (carpeta / "dibujo.png").exists():
        print(f"Aviso: falta {rel}/dibujo.png; el README va a mostrar la imagen rota.")

    if url:
        problema["video"] = url
        readme = carpeta / "README.md"
        texto = readme.read_text(encoding="utf-8")
        if MARCA_VIDEO in texto:
            readme.write_text(texto.replace(MARCA_VIDEO, url), encoding="utf-8")
    problema["estado"] = "publicado"
    guardar_problemas(problemas)
    generar_indice.main()

    if "--sin-commit" in opciones:
        return
    if git("rev-parse", "--is-inside-work-tree").returncode != 0:
        print("Esta carpeta no es un repo de git, así que no hice commit.")
        return
    git("add", rel, "problemas.csv", "README.md", f"{problema['carpeta']}/README.md")
    if git("diff", "--cached", "--quiet").returncode == 0:
        print("No había cambios nuevos para commitear.")
        return
    mensaje = (f"{numero} {problema['titulo']} "
               f"({problema['patron'].lower()}, {problema['dificultad'].lower()})")
    resultado = git("commit", "-m", mensaje)
    if resultado.returncode != 0:
        print(resultado.stdout + resultado.stderr)
        sys.exit("No se pudo hacer el commit (mirá el error de arriba).")
    print(f"Commit: {mensaje}")
    print("Subilo con: git push")


if __name__ == "__main__":
    main()
