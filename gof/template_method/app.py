"""
Template Method
- スーパークラスで処理の枠組みを定め、サブクラスでその具体的内容を定める
- 処理フローの全体構造を変えずに、処理の一部のみ変更したい時に有効
"""

from abc import ABCMeta, abstractmethod


class UnitTestTemplate(metaclass=ABCMeta):
    def test(self):
        self.setup()
        self.execute()
        self.down()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def down(self):  # 共通処理
        print("down")


class UserTest(UnitTestTemplate):
    def setup(self):
        print("setup: UserTest")

    def execute(self):
        print("execute: UserTest")


if __name__ == '__main__':
    user_test = UserTest()
    user_test.test()
