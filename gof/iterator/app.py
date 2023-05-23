"""
Iterator
- コレクションの内部構造を利用者に見せずに、要素を順番にアクセスする方法
- コレクションと探索の振る舞いを分離する
"""

from abc import ABCMeta, abstractmethod


class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.id}: {self.name}'


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def get_iterator(self) -> Iterator:
        pass


class UserRoom(Aggregate):
    def __init__(self):
        self.__users = []

    def add_user(self, user: User) -> None:
        self.__users.append(user)

    def get_users(self) -> list[User]:
        return self.__users

    def get_count(self) -> int:
        return len(self.__users)

    def get_iterator(self) -> Iterator:
        return UserRoomIterator(self)


class UserRoomIterator(Iterator):
    def __init__(self, user_room: UserRoom):
        self.__user_room = user_room
        self.__current = 0

    def has_next(self) -> bool:
        return self.__current < self.__user_room.get_count()

    def next(self):
        if not self.has_next():
            raise Exception('no more user')
        user = self.__user_room.get_users()[self.__current]
        self.__current += 1
        return user


if __name__ == '__main__':
    user_room = UserRoom()
    user_room.add_user(User(1, 'John'))
    user_room.add_user(User(2, 'Mike'))

    iterator = user_room.get_iterator()
    while iterator.has_next():
        print(iterator.next())

    print(iterator.next())  # もういないのでエラー
