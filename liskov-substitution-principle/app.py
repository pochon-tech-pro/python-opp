"""
Liskov Substitution Principle: リスコフの置換原則
サブクラスは、そのスーパークラスの代用ができなければならない
TクラスのインスタンスXで実行できるならば、TクラスのサブクラスSのインスタンスYでも実行できなければならない
サブクラスとスーパークラスの間で実行できるものできないものが存在すると、サブクラスを全て理解しなければならない（リスコフの置換原則違反）
"""


class Rectangle:  # 長方形
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        self._width = width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        self._height = height

    def area(self) -> int:  # 面積を返す（幅 * 高さ）
        return self._width * self._height


class Square(Rectangle):  # 正方形（数学的には長方形の一部なので継承してしまった）
    def __init__(self, size: int) -> None:
        super().__init__(size, size)

    # 正方形は、幅と高さが同じでなければならないので、それを保証するために、上書きをしている
    # @width.setterではない理由は、Pythonの仕様上、@propertyでGetterを定義しないとエラーになるから再定義で楽してる。
    @Rectangle.width.setter
    def width(self, width: int) -> None:
        self._width = self._height = width

    # 正方形は、幅と高さが同じでなければならないので、それを保証するために、上書きをしている
    @Rectangle.height.setter
    def height(self, height: int) -> None:
        self._width = self._height = height


def print_area(obj) -> None:
    change_to_width = 100
    change_to_height = 20
    obj.width = change_to_width
    obj.height = change_to_height
    expected = change_to_width * change_to_height
    print("Expected an area of {}, Actual an area of {}".format(expected, obj.area()))


if __name__ == '__main__':
    print_area(Rectangle(2, 3))  # 継承元が実行できるならば
    print_area(Square(5))  # 継承先も実行できなければならない（できてないので違反している）
