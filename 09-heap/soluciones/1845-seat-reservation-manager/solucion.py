# 1845. Seat Reservation Manager (Media)
# https://leetcode.com/problems/seat-reservation-manager/
#
# Idea: un min-heap con los asientos que se liberaron y un contador con el próximo asiento nunca
#       usado; reservar toma el menor de los dos.
# Tiempo: O(log n) por operación · Espacio: O(n)

import heapq


class SeatManager:
    def __init__(self, n: int):
        self.liberados = []
        self.siguiente = 1

    def reserve(self) -> int:
        if self.liberados:
            return heapq.heappop(self.liberados)
        self.siguiente += 1
        return self.siguiente - 1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.liberados, seatNumber)


if __name__ == "__main__":
    m = SeatManager(5)
    assert m.reserve() == 1
    assert m.reserve() == 2
    m.unreserve(2)
    assert m.reserve() == 2
    assert [m.reserve() for _ in range(3)] == [3, 4, 5]
    m.unreserve(5)
    m.unreserve(3)
    assert m.reserve() == 3
    print("OK")
