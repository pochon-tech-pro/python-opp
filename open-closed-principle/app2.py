from typing import List, TypeVar
from abc import ABCMeta, abstractmethod

# TはAbstractComparatorまたはそのサブクラスの型を持つことが保証される
T = TypeVar('T', bound='AbstractComparator')


class MemberInfo:
    def __init__(self, name: str, job: str, country: str) -> None:
        self.name = name
        self.job = job
        self.country = country

    def __str__(self) -> str:
        return f'{self.name}, {self.job}, {self.country}'


class AbstractComparator(metaclass=ABCMeta):
    @abstractmethod
    def is_satisfied(self, other: MemberInfo) -> bool:
        pass

    # -> 'AndComparator' という文字列形式で指定しているのは、この時点ではAndComparatorクラスが定義されていないため
    # これを、forward referenceと呼ぶ
    def __and__(self: T, other: T) -> 'AndComparator':
        # 自身と他のComparatorを引数に、AndComparatorを生成して返す
        return AndComparator([self, other])

    def __or__(self: T, other: T) -> 'OrComparator':
        return OrComparator([self, other])


class AndComparator(AbstractComparator):
    # AndComparatorは、元の2つのComparator（自身と他のComparator）を保持する
    def __init__(self, comparators) -> None:
        self.comparators = comparators

    def is_satisfied(self, other: MemberInfo) -> bool:
        # 全てが等しい場合にTrueを返す
        return all(comparator.is_satisfied(other) for comparator in self.comparators)


class OrComparator(AbstractComparator):
    def __init__(self, comparators: List[T]) -> None:
        self.comparators = comparators

    def is_satisfied(self, other: MemberInfo) -> bool:
        # どれかが等しい場合にTrueを返す
        return any(comparator.is_satisfied(other) for comparator in self.comparators)


class AbstractFilter(metaclass=ABCMeta):
    @abstractmethod
    def filter(self, others: List[MemberInfo], comparator: AbstractComparator) -> List[MemberInfo]:
        pass


# Jobで絞り込むクラス
class JobComparator(AbstractComparator):
    def __init__(self, job: str) -> None:
        self.job = job

    def is_satisfied(self, other: MemberInfo) -> bool:
        print("JobComparator.is_satisfied() called. self:{}, other:{}".format(self.job, other.job))
        return other.job == self.job


# Countryで絞り込むクラス
class CountryComparator(AbstractComparator):
    def __init__(self, country: str) -> None:
        self.country = country

    def is_satisfied(self, other: MemberInfo) -> bool:
        print("CountryComparator.is_satisfied() called. self:{}, other:{}".format(self.country, other.country))
        return other.country == self.country


# 絞り込み用のクラス
class MemberFilter(AbstractFilter):
    def filter(self, others: List[MemberInfo], comparator: AbstractComparator) -> List[MemberInfo]:
        # return [other for other in others if comparator.is_satisfied(other)]
        for other in others:
            print("MemberFilter.filter() called. other:{}".format(other))
            if comparator.is_satisfied(other):
                yield other


if __name__ == '__main__':
    member1 = MemberInfo('John', 'プログラマー', 'アメリカ')
    member2 = MemberInfo('太郎', 'プログラマー', '日本')

    members = [member1, member2]

    member_filter = MemberFilter()
    programmer_comparator = JobComparator('プログラマー')
    usa_comparator = CountryComparator('日本')
    programmer_and_usa = programmer_comparator & usa_comparator  # AndComparatorが返される
    for member in member_filter.filter(members, programmer_and_usa):
        print(member)
