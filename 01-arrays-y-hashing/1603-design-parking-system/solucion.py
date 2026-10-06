# 1603. Design Parking System (Fácil)
# https://leetcode.com/problems/design-parking-system/
#
# Idea: guardo cuántos lugares libres quedan de cada tamaño; addCar descuenta si hay lugar.
# Tiempo: O(1) por operación · Espacio: O(1)

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.libres = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.libres[carType] == 0:
            return False
        self.libres[carType] -= 1
        return True


if __name__ == "__main__":
    p = ParkingSystem(1, 1, 0)
    assert p.addCar(1) is True
    assert p.addCar(2) is True
    assert p.addCar(3) is False
    assert p.addCar(1) is False
    print("OK")
