"""
Singleton
- インスタンスが1つしか存在しないことを保証する
- メモリ効率が良い（現代のPC端末ではメリットにならない）
- マルチスレッドでの扱いがロックとか使わないといけない
- 状態は持たせないようにすべき
- コンストラクタがprivate
- pythonはコンストラクタがprivateにできないので、クラス変数で補う
"""

import datetime


class Logger:
    __instance = None

    # インスタンスが作成される前に呼び出される（__init__は後）
    def __new__(cls):
        if cls.__instance is None:
            # super().__new__(cls) でインスタンスを作成
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def log(self, msg: str) -> None:
        now = datetime.datetime.now()
        print("{}: {}".format(now, msg))


if __name__ == '__main__':
    logger1 = Logger()
    logger2 = Logger()
    print(logger1)
    print(logger2)
    print(logger1 is logger2)
    logger1.log('log message 1')
    logger2.log('log message 2')
