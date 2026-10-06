# 1396. Design Underground System (Media)
# https://leetcode.com/problems/design-underground-system/
#
# Idea: un diccionario con quién entró dónde y cuándo; al salir, sumo el tiempo del viaje a (origen, destino) junto con la cantidad de viajes.
# Tiempo: O(1) por operación · Espacio: O(P + S²), pasajeros y pares de estaciones

from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.entradas = {}
        self.viajes = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.entradas[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        origen, inicio = self.entradas.pop(id)
        datos = self.viajes[(origen, stationName)]
        datos[0] += t - inicio
        datos[1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cantidad = self.viajes[(startStation, endStation)]
        return total / cantidad


if __name__ == "__main__":
    u = UndergroundSystem()
    u.checkIn(45, "Leyton", 3)
    u.checkIn(32, "Paradise", 8)
    u.checkIn(27, "Leyton", 10)
    u.checkOut(45, "Waterloo", 15)
    u.checkOut(27, "Waterloo", 20)
    u.checkOut(32, "Cambridge", 22)
    assert u.getAverageTime("Paradise", "Cambridge") == 14.0
    assert u.getAverageTime("Leyton", "Waterloo") == 11.0
    u.checkIn(10, "Leyton", 24)
    assert u.getAverageTime("Leyton", "Waterloo") == 11.0
    u.checkOut(10, "Waterloo", 38)
    assert u.getAverageTime("Leyton", "Waterloo") == 12.0
    print("OK")
