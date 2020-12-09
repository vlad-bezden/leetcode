class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Sea:
    def __init__(self, ships, top_right, bottom_left) -> None:
        self.ships = ships
        self.top_right = top_right
        self.bottom_left = bottom_left

    def hasShips(self, topRight: Point, bottomLeft: Point) -> bool:
        """Check if there is at least one ship inside of rectangle.

        Check if rectangle inside of the sea
        and if there is any ships inside of that rectangle.
        """
        for ship in self.ships:
            if (
                bottomLeft.x <= ship[0] <= topRight.x
                and bottomLeft.y <= ship[1] <= topRight.y
            ):
                return True
        return False


class Solution:
    def countShips(self, sea: Sea, topRight: Point, bottomLeft: Point) -> int:
        ships = 0

        def calculate(tr_x, tr_y, bl_x, bl_y):
            if sea.hasShips(Point(tr_x, tr_y), Point(bl_x, bl_y)):
                if tr_x == bl_x and tr_y == bl_y:
                    # that is the point, no more divide
                    return 1
                elif tr_y - bl_y < tr_x - bl_x:
                    # horizontal rectangle
                    middle_x = (tr_x + bl_x) // 2
                    return calculate(tr_x, tr_y, middle_x + 1, bl_y) + calculate(
                        middle_x, tr_y, bl_x, bl_y
                    )
                else:
                    # vertical rectangle
                    middle_y = (bl_y + tr_y) // 2
                    return calculate(tr_x, tr_y, bl_x, middle_y + 1) + calculate(
                        tr_x, middle_y, bl_x, bl_y
                    )
            return 0

        ships += calculate(topRight.x, topRight.y, bottomLeft.x, bottomLeft.y)
        return ships


if __name__ == "__main__":
    ships = [[1, 1], [2, 2], [3, 3], [5, 5]]
    top_right = Point(4, 4)
    bottom_left = Point(0, 0)
    sea = Sea(ships, top_right, bottom_left)

    solution = Solution()
    output = solution.countShips(sea, top_right, bottom_left)
    expected = 3
    assert output == expected, f"{output = }, {expected = }"

    print("PASSED!!!")
