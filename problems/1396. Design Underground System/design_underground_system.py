class UndergroundSystem:
    def __init__(self) -> None:
        self._current_rides = {}
        self._rides_stats = {}

    def checkIn(self, id: int, start_station_name: str, start_time: int) -> None:
        self._current_rides[id] = (start_station_name, start_time)

    def checkOut(self, id: int, end_station_name: str, end_time: int) -> None:
        start_station_name, start_time = self._current_rides.pop(id)
        ride_name = (start_station_name, end_station_name)
        total, rides = self._rides_stats.get(ride_name, (0, 0))
        self._rides_stats[ride_name] = (
            total + end_time - start_time,
            rides + 1,
        )

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ride_total_time, rides = self._rides_stats[(startStation, endStation)]
        return ride_total_time / rides


if __name__ == "__main__":
    # example 1
    obj = UndergroundSystem()
    obj.checkIn(45, "Leyton", 3)
    obj.checkIn(32, "Paradise", 8)
    obj.checkIn(27, "Leyton", 10)
    obj.checkOut(45, "Waterloo", 15)
    obj.checkOut(27, "Waterloo", 20)
    obj.checkOut(32, "Cambridge", 22)
    assert obj.getAverageTime("Paradise", "Cambridge") == 14
    assert obj.getAverageTime("Leyton", "Waterloo") == 11
    obj.checkIn(10, "Leyton", 24)
    assert obj.getAverageTime("Leyton", "Waterloo") == 11
    obj.checkOut(10, "Waterloo", 38)
    obj.getAverageTime("Leyton", "Waterloo") == 12

    # example 2
    obj = UndergroundSystem()
    obj.checkIn(10, "Leyton", 3)
    obj.checkOut(10, "Paradise", 8)
    assert obj.getAverageTime("Leyton", "Paradise") == 5.0
    obj.checkIn(5, "Leyton", 10)
    obj.checkOut(5, "Paradise", 16)
    assert obj.getAverageTime("Leyton", "Paradise") == 5.5
    obj.checkIn(2, "Leyton", 21)
    obj.checkOut(2, "Paradise", 30)
    from math import isclose

    assert isclose(obj.getAverageTime("Leyton", "Paradise"), 6.66667, abs_tol=10 ** -5)

    print("PASSED!!!")
