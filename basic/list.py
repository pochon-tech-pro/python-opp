"""
リスト内包表記
ループと条件を使い、1行でリストを作成する方法
"""


# リスト内包表記を使わない場合
def fn1(_target: list) -> list:
    new_list = []
    for i in range(len(_target)):
        if type(_target[i]) == int:
            new_list.append(_target[i])
    return new_list


# リスト内包表記を使う場合
def fn2(_target: list) -> list:
    return [each for each in _target if type(each) == int]


if __name__ == '__main__':
    origin = [1, 2, 'ABC', 4]
    print(fn1(origin))
    print(fn2(origin))
