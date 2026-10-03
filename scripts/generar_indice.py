#!/usr/bin/env python3
"""Regenera las tablas del README principal y de cada patrón desde problemas.csv.

Uso: python3 scripts/generar_indice.py
No hace falta correrlo a mano después de publicar.py: ya lo corre solo.
"""
from comun import RAIZ, EMOJI, leer_problemas, carpeta_de, preparar_consola

INICIO_INDICE, FIN_INDICE = "<!-- indice:inicio -->", "<!-- indice:fin -->"
INICIO_PATRON, FIN_PATRON = "<!-- problemas:inicio -->", "<!-- problemas:fin -->"
ENCABEZADO = "| # | Problema | Dificultad | Video | Solución |\n|---:|---|---|:---:|:---:|"


def reemplazar_bloque(ruta, inicio, fin, contenido):
    """Reemplaza lo que hay entre los marcadores y deja intacto el resto del archivo."""
    texto = ruta.read_text(encoding="utf-8") if ruta.exists() else ""
    bloque = f"{inicio}\n{contenido}\n{fin}"
    if inicio in texto and fin in texto:
        antes, resto = texto.split(inicio, 1)
        despues = resto.split(fin, 1)[1]
        nuevo = antes + bloque + despues
    else:
        nuevo = (texto.rstrip("\n") + "\n\n" if texto else "") + bloque + "\n"
    if nuevo != texto:
        ruta.write_text(nuevo, encoding="utf-8")


def fila(problema, prefijo):
    titulo = problema["titulo"].replace("|", "\\|")
    if problema["lista"] == "Blind 75":
        titulo += " ⭐"
    dificultad = f"{EMOJI.get(problema['dificultad'], '')} {problema['dificultad']}"
    video = f"[▶️]({problema['video']})" if problema["video"] else "🔜"
    carpeta = carpeta_de(problema)
    if (carpeta / "solucion.py").exists():
        solucion = f"[Python]({prefijo}{carpeta.name}/)"
    else:
        solucion = "🔜"
    return (f"| {int(problema['numero'])} | [{titulo}]({problema['enunciado']}) "
            f"| {dificultad} | {video} | {solucion} |")


def tabla(problemas, prefijo):
    return ENCABEZADO + "\n" + "\n".join(fila(p, prefijo) for p in problemas)


def main():
    preparar_consola()
    problemas = sorted(leer_problemas(), key=lambda p: (p["carpeta"], int(p["orden_plan"])))
    publicados = [p for p in problemas if p["estado"] == "publicado"]

    def avance(dificultad):
        total = sum(1 for p in problemas if p["dificultad"] == dificultad)
        hechos = sum(1 for p in publicados if p["dificultad"] == dificultad)
        return f"{EMOJI[dificultad]} {hechos}/{total}"

    patrones = {}
    for p in problemas:
        patrones.setdefault((p["carpeta"], p["patron"]), []).append(p)

    partes = [
        "## Progreso",
        f"**{len(publicados)} / {len(problemas)} publicados** · "
        f"{avance('Fácil')} · {avance('Media')} · {avance('Difícil')}",
        "",
        "## Ejercicios por patrón",
    ]
    for i, ((carpeta, patron), lista) in enumerate(patrones.items(), 1):
        hechos = sum(1 for p in lista if p["estado"] == "publicado")
        partes += [
            "",
            "<details>",
            f"<summary><b>{i}. {patron}</b> · {hechos}/{len(lista)}</summary>",
            "",
            f"[Explicación y plantilla del patrón]({carpeta}/)",
            "",
            tabla(lista, f"{carpeta}/"),
            "",
            "</details>",
        ]
        reemplazar_bloque(RAIZ / carpeta / "README.md", INICIO_PATRON, FIN_PATRON, tabla(lista, ""))

    reemplazar_bloque(RAIZ / "README.md", INICIO_INDICE, FIN_INDICE, "\n".join(partes))
    print(f"Índice actualizado: {len(publicados)}/{len(problemas)} publicados.")


if __name__ == "__main__":
    main()
