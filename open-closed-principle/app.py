"""
OpenClosedPrinciple: 拡張しやすく修正はしないようにすべき。
機能拡張が容易だったり、元のソースコードのテストが不要になる。
"""

from typing import List


# Member情報を持つ役割クラス
class MemberInfo:
    def __init__(self, name: str, job: str, country: str) -> None:
        self.name = name
        self.job = job
        self.country = country

    def __str__(self) -> str:
        return f'{self.name}, {self.job}, {self.country}'


# OCP違反の例
class BadMemberFilter:
    @staticmethod
    def filter_by_job(_members: List[MemberInfo], _job: str) -> List[MemberInfo]:
        return [target for target in _members if target.job == _job]

    @staticmethod
    def filter_by_country(_members: List[MemberInfo], _country: str) -> List[MemberInfo]:
        return [target for target in _members if target.country == _country]

    # jobとcountryの両方で絞り込みたい時は？年齢が増えて絞り込みたくなったらどうする？
    # クラスを編集してメソッドを追加するなりしていく必要が出てきてしまう。


"""
OCPを検討した例
"""

from abc import ABCMeta, abstractmethod


# 比較用の抽象クラス
class AbstractComparator(metaclass=ABCMeta):
    @abstractmethod
    def is_satisfied(self, other: MemberInfo) -> bool:
        pass


# 絞り込み用の抽象クラス
class AbstractFilter(metaclass=ABCMeta):
    @abstractmethod
    def filter(self, others: List[MemberInfo], comparator: AbstractComparator) -> List[MemberInfo]:
        pass


# Jobで絞り込むクラス
class JobComparator(AbstractComparator):
    def __init__(self, job: str) -> None:
        self.job = job

    def is_satisfied(self, other: MemberInfo) -> bool:
        return other.job == self.job


# Countryで絞り込むクラス
class CountryComparator(AbstractComparator):
    def __init__(self, country: str) -> None:
        self.country = country

    def is_satisfied(self, other: MemberInfo) -> bool:
        return other.country == self.country


# 絞り込み用のクラス
class MemberFilter(AbstractFilter):
    def filter(self, others: List[MemberInfo], comparator: AbstractComparator) -> List[MemberInfo]:
        return [other for other in others if comparator.is_satisfied(other)]


# 仕事と国の絞り込みをしたくなったとしても下記のクラスを追加するだけで済む
class JobAndCountryComparator(AbstractComparator):
    def __init__(self, job: str, country: str) -> None:
        self.job = job
        self.country = country

    def is_satisfied(self, other: MemberInfo) -> bool:
        return other.job == self.job and other.country == self.country


if __name__ == '__main__':
    member1 = MemberInfo('John', 'Programmer', 'USA')
    member2 = MemberInfo('Mike', 'Designer', 'USA')
    member3 = MemberInfo('Jane', 'Programmer', 'Japan')

    members = [member1, member2, member3]

    for target in BadMemberFilter.filter_by_job(members, 'Programmer'):
        print(target)
    for target in BadMemberFilter.filter_by_country(members, 'USA'):
        print(target)

    print("------------------")

    # OCPを検討した例
    member_filter = MemberFilter()
    programmer_comparator = JobComparator('Programmer')
    for target in member_filter.filter(members, programmer_comparator):
        print(target)
    japan_comparator = CountryComparator('Japan')
    for target in member_filter.filter(members, japan_comparator):
        print(target)

    print("------------------")
    programmer_and_japan_comparator = JobAndCountryComparator('Programmer', 'Japan')
    for target in member_filter.filter(members, programmer_and_japan_comparator):
        print(target)
