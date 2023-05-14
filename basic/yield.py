from typing import Union, Iterator, Generator


# int型とstr型の値を順に生成するので、Union[int, str]と思われがちだが、
# def func(cnt: int) -> Union[int, str]:
# ジェネレータ関数のため、戻り値の型はIterator[Union[int, str]]となる
def func(cnt: int) -> Iterator[Union[int, str]]:
    for v1 in range(cnt):
        yield v1

    for v2 in range(cnt):
        yield "".join([str(v2), "a"])


# send、throwやcloseを使う場合は、Generatorを使う
# def send_sample(cnt: int) -> Iterator[int]:
def send_sample(cnt: int) -> Generator[int, Union[int, str], None]:
    for i in range(cnt):
        try:
            print("send_sample_start: i = {}".format(i))
            x = yield i  # nextの後にsendを使うと、値を受け取れる
            print("yield execute x = {}".format(x))
        except ValueError as e:
            print("ValueError: {}".format(e))


if __name__ == '__main__':
    fn = func(2)
    print(next(fn))
    print(next(fn))
    print(next(fn))
    print(next(fn))
    # print(next(fn))  # StopIteration

    # for in を使い、nextを使わない方法
    for i in func(2):
        print(i)
        print(type(i))

    se = send_sample(3)
    next(se)
    se.send(100)  # 値を送出する
    next(se)
    se.send("文字列")  # 値を送出する
    # se.throw(ValueError, "Invalid value !!!!!!!!!!!!!")  # 例外を送出する
    se.close()
    # next(se)  # StopIteration
