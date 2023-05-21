"""
リスコフの置換原則のもっとわかりやすい例
リスコフの置換原則とは、サブクラスはそのスーパークラスを置換可能でなければならないというもの
つまり、サブクラスのインスタンスはスーパークラスのインスタンスとして使用できるべきということ

違反例：
例えば、鳥クラスとペンギンクラスがあるとする。
ほとんどの鳥は飛ぶことができるので、鳥クラスには飛ぶというメソッドがあるは正しそうに見える
しかし、ペンギンは飛ぶことができない。
したがって、ペンギンは飛べない旨をオーバーライドする必要がある。

このように、鳥クラスのインスタンスが期待する飛ぶ振る舞いと、ペンギンクラスの飛ぶ振る舞いが異なるため、完全に置換できない
"""


class Bird:
    def fly(self):
        return "I can fly!"


class Penguin(Bird):
    def fly(self):
        return "I can't fly!"


# 鳥なんだから飛べるだろうとを期待した関数（予期しない振る舞いが発生する例）
def let_it_fly(bird):
    print(bird.fly())


"""
上記を回避したい場合は、飛ぶ能力を持つ鳥類クラスを作成し、鳥クラスとペンギンクラスはそれを継承する
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"

class Penguin(Bird):
    pass
"""

if __name__ == '__main__':
    bird = Bird()
    print(bird.fly())
    penguin = Penguin()
    print(penguin.fly())
