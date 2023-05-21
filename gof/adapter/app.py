"""
Adapter
- 既存のクラスを新しいインターフェースに適合させる
- 既存のクラスに修正がいらないので、既存のクラスを使っているコードに影響がない
    - 実績のあるクラスに手を加えずに再利用したい時に利用するのに便利
- 実装方法は、継承によるものと委譲によるもがある
    - 迷ったら移譲が良い：リスコフの置換原則違反に注意しながら適合を考えないといけないため
- 利用者は、IFに関心はなくビジネスロジックのみに関心があり、IFに関心があるのは開発者であるので、ここを分離することで単一責任の原則を満たせる
    - 単一責任の原則：アクターが異なるクラスは、アクターごとに分離すべき
"""

from abc import ABCMeta, abstractmethod


class Target(metaclass=ABCMeta):
    @abstractmethod
    def get_csv_data(self):
        pass


class JsonLibrary:
    def get_json_data(self) -> list[dict[str, str]]:
        return [{'name': 'Taro', 'age': '20'}, {'name': 'Jiro', 'age': '30'}]


class JsonToCSVAdapter(Target, JsonLibrary):  # 継承によるAdapter
    def get_csv_data(self):
        json_data = self.get_json_data()
        header = ",".join(json_data[0].keys()) + "\n"
        values = [",".join(d.values()) for d in json_data]
        body = "\n".join(values)
        return header + body


class JsonToCSVAdapter2(Target):  # 移譲によるAdapter
    def __init__(self, adaptee: JsonLibrary):
        self.__adaptee = adaptee

    def get_csv_data(self):
        json_data = self.__adaptee.get_json_data()
        header = ",".join(json_data[0].keys()) + "\n"
        values = [",".join(d.values()) for d in json_data]
        body = "\n".join(values)
        return header + body

    def get_json_data(self):
        return self.__adaptee.get_json_data()


if __name__ == '__main__':
    adaptee = JsonLibrary()
    print(adaptee.get_json_data())

    print("-----------------------------")
    adapter = JsonToCSVAdapter()
    print(adapter.get_json_data())
    print(adapter.get_csv_data())

    print("-----------------------------")
    adapter2 = JsonToCSVAdapter2(adaptee)
    print(adapter2.get_json_data())
    print(adapter2.get_csv_data())
