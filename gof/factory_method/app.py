"""
Factory Method
"""

from abc import ABCMeta, abstractmethod


class Drink(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        pass


class PETBottle(Drink):
    def __str__(self):
        return 'PET Bottle !!'


class Can(Drink):
    def __str__(self):
        return 'Can !!'


class DrinkFactory(metaclass=ABCMeta):
    def create(self) -> Drink:
        self.washing()
        drink = self.produce()
        self.packing()
        return drink

    def washing(self) -> None:
        print('Washing...')

    @abstractmethod  # 製造工程のみ造られる飲料水によって異なるので、サブクラスで実装する
    def produce(self) -> Drink:
        pass

    def packing(self):
        print('Packing...')


class PETBottleFactory(DrinkFactory):
    def produce(self) -> PETBottle:
        print('PETBottle producing...')
        return PETBottle()


class CanFactory(DrinkFactory):
    def produce(self) -> Can:
        print('Can producing...')
        return Can()


if __name__ == '__main__':
    pet_factory = PETBottleFactory()
    print(pet_factory.create())

    can_factory = CanFactory()
    print(can_factory.create())
