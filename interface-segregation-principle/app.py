"""
Interface Segregation Principle: インターフェース分離の原則
インターフェースに必要のないメソッドを追加して、継承先が無駄なコードをわざわざ実装しないといけないようなことを避ける
インターフェースを細分化することで、クライアントが実装しなければならないメソッドを明確にする
単一責任の原則と似ているが、こちらはインターフェースに関する原則
"""

from abc import ABCMeta, abstractmethod


class BadSportsAthlete(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def run(self):
        pass


class BadSwimmer(BadSportsAthlete):
    def swim(self):
        print('泳ぐ')

    def run(self):  # 無駄（バグの温床）
        pass


class BadRunner(BadSportsAthlete):
    def swim(self):  # 無駄（バグの温床）
        pass

    def run(self):
        print('走る')


"""
違反解決例
"""


class SportsAthlete(metaclass=ABCMeta):
    pass


class SwimAthlete(SportsAthlete):
    @abstractmethod
    def swim(self):
        pass


class RunAthlete(SportsAthlete):
    @abstractmethod
    def run(self):
        pass


class ConcreteSwimmer(SwimAthlete):
    def swim(self):
        print('泳ぐ')


class ConcreteRunner(RunAthlete):
    def run(self):
        print('走る')


class ConcreteSwimmerRunner(SwimAthlete, RunAthlete):  # 両方実装したい時は、多重継承を使う
    def swim(self):
        print('泳ぐ')

    def run(self):
        print('走る')


if __name__ == '__main__':
    swimmer = BadSwimmer()
    swimmer.swim()
    runner = BadRunner()
    runner.run()
    print('------------------')
    swimmer = ConcreteSwimmer()
    swimmer.swim()
    runner = ConcreteRunner()
    runner.run()
