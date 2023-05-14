from abc import ABC, abstractmethod


class Shape(ABC):  # 抽象クラス
    @abstractmethod
    def area(self) -> int:
        pass

    @abstractmethod
    def set_size(self, width: int, height: int) -> None:
        pass


class Rectangle(Shape):  # 長方形
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def set_size(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def area(self) -> int:  # 面積を返す（幅 * 高さ）
        return self._width * self._height


class Square(Shape):  # 正方形
    def __init__(self, size: int) -> None:
        self._size = size

    @property
    def size(self) -> int:
        return self._size

    def set_size(self, width: int, height: int) -> None:
        if width != height:
            # 正方形は、幅と高さが同じでなければならないので、それを保証するために、エラーを出す
            raise ValueError("In a square, width and height must be the same.")
        self._size = width

    def area(self) -> int:  # 面積を返す（サイズ * サイズ）
        return self._size * self._size


def print_area(obj, change_to_width: int, change_to_height: int) -> None:
    obj.set_size(change_to_width, change_to_height)
    expected = change_to_width * change_to_height
    print("Expected an area of {}, Actual an area of {}".format(expected, obj.area()))


if __name__ == '__main__':
    print_area(Rectangle(2, 3), 4, 5)
    print_area(Square(5), 4, 4)
