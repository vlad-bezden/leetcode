"""1603. Design Parking System.

Level: Easy

https://leetcode.com/problems/design-parking-system/
"""

from dataclasses import dataclass
from enum import IntEnum


class CarType(IntEnum):
    Big = 1
    Medium = 2
    Small = 3


@dataclass
class ParkingSystem:
    big: int
    medium: int
    small: int

    def addCar(self, carType: CarType) -> bool:
        if carType == CarType.Big and self.big > 0:
            self.big -= 1
            return True
        elif carType == CarType.Medium and self.medium > 0:
            self.medium -= 1
            return True
        elif carType == CarType.Small and self.small > 0:
            self.small -= 1
            return True

        return False
