from typing import Union, Iterator


# int型とstr型の値を順に生成するので、Union[int, str]と思われがちだが、
# def func(cnt: int) -> Union[int, str]:
# ジェネレータ関数のため、戻り値の型はIterator[Union[int, str]]となる
def func(cnt: int) -> Iterator[Union[int, str]]:
    for v1 in range(cnt):
        yield v1

    for v2 in range(cnt):
        yield "".join([str(v2), "a"])


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
