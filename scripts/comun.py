"""Funciones que comparten los scripts del repo."""
import csv
import os
import sys
from pathlib import Path

COMANDO_PY = "python" if os.name == "nt" else "python3"
RAIZ = Path(__file__).resolve().parent.parent
CSV_PROBLEMAS = RAIZ / "problemas.csv"
COLUMNAS = [
    "orden_plan", "numero", "slug", "titulo", "patron", "carpeta",
    "dificultad", "lista", "enunciado", "video_neetcode", "video", "estado",
]
EMOJI = {"Fácil": "🟢", "Media": "🟡", "Difícil": "🔴"}


def preparar_consola():
    """Evita errores con tildes y emojis en la consola de Windows."""
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def leer_problemas():
    with open(CSV_PROBLEMAS, encoding="utf-8", newline="") as archivo:
        return list(csv.DictReader(archivo))


def guardar_problemas(problemas):
    with open(CSV_PROBLEMAS, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS, lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(problemas)


def buscar(problemas, numero):
    for problema in problemas:
        if int(problema["numero"]) == numero:
            return problema
    return None


def carpeta_de(problema):
    return RAIZ / problema["carpeta"] / "soluciones" / f"{int(problema['numero']):04d}-{problema['slug']}"
