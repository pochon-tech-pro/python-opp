"""
Dependency Inversion Principle: 依存性逆転の原則
上位モジュールは下位モジュールに依存してはいけない
両者は抽象化に依存すべきであり、具象化に依存してはいけない
"""


class BadBook:
    def __init__(self, content: str) -> None:
        self.content = content


class BadFormatter:
    # 具象クラスであるBadBookクラスに依存している
    def format(self, book: BadBook) -> str:
        return book.content


class BadPrinter:
    def print(self, book: BadBook) -> None:
        formatter = BadFormatter()  # 具象化に依存している
        formatted_book = formatter.format(book)
        print(formatted_book)


"""
違反解決例
"""
from abc import ABCMeta, abstractmethod, abstractproperty


class Book(metaclass=ABCMeta):
    @abstractproperty
    def content(self) -> str:
        pass


class PaperBook(Book):
    def __init__(self, content: str) -> None:
        self._content = content

    @property
    def content(self) -> str:
        return self._content


class EBook(Book):
    def __init__(self, content: str) -> None:
        self._content = content

    @property
    def content(self) -> str:
        return 'E' + self._content


class Formatter(metaclass=ABCMeta):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class HtmlFormatter(Formatter):
    # 抽象クラスを受け取るようになった
    def format(self, book: Book) -> str:
        return f'<html>{book.content}</html>'


# 拡張も容易になった（Open-Closed Principleも満たしている）
class XMLFormatter(Formatter):
    def format(self, book: Book) -> str:
        return f'<xml>{book.content}</xml>'


class Printer:
    # 抽象クラスを受け取るようになった
    def __init__(self, formatter: Formatter) -> None:
        self._formatter = formatter

    def print(self, book: Book) -> None:
        formatted_book = self._formatter.format(book)
        print(formatted_book)


if __name__ == '__main__':
    book = BadBook('ピーターパン')
    printer = BadPrinter()
    printer.print(book)

    book = PaperBook('ピーターパン')
    html_printer = Printer(HtmlFormatter())
    html_printer.print(book)
    xml_printer = Printer(XMLFormatter())
    xml_printer.print(book)
    ebook = EBook('ピーターパン')
    html_printer.print(ebook)
    xml_printer.print(ebook)
