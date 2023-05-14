class Info:
    pass


# Member情報を持つ役割クラス
class MemberInfo(Info):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

    # MemberInfoクラスなのに、ファイルに書き込む処理が入っている（役割が多い）
    # def write_file(self, filename):
    #     with open(filename, 'w') as f:
    #         f.write(str(self))


# Manager情報を持つ役割クラス
class ManagerInfo(Info):
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return f'{self.name}, {self.age}, {self.tel}'


# ファイル操作に関する役割を持つクラス
class FileManager:
    @staticmethod
    def write_str_info(info: Info, filename: str):
        with open(filename, 'w') as f:
            f.write(f"{str(info)}\n")

    @staticmethod
    def append_str_info(info: Info, filename: str):
        with open(filename, 'a') as f:
            f.write(f"{str(info)}\n")


if __name__ == '__main__':
    member = MemberInfo('John', 22)
    manager = ManagerInfo('Mike', 30, '010-1234-5678')
    print(member)
    print(manager)
    # member.write_file('member.txt')

    FileManager.write_str_info(member, 'member.txt')
    FileManager.write_str_info(manager, 'manager.txt')

    FileManager.append_str_info(member, 'member.txt')
    FileManager.append_str_info(manager, 'manager.txt')
