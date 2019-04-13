import abc
'''
Allow a request to pass down a chain of receivers until it is handled.

object oriented version of `if ... elif ... elif ... else ...` idiom, 
condition–action blocks can be rearranged and reconfigured at runtime.

主要精神：降低 "要求端" & "處理端" 間的耦合性，個別成為獨立的零件

自由組合處理請求的物件為一個鏈，避免請求的發送者與接收者之間的耦合關係，
沿著鏈傳遞該請求，每個物件處理 & 決定是否傳遞給下一個處理物件。
'''


class Handler:
    def __init__(self, next):
        self.next = next

    def doNext(self, c):
        if self.next:
            self.next.handle(c)


class SymbolHandler(Handler):
    def __init__(self, next):
        Handler.__init__(self, next)

    def handle(self, c):
        print("Symbol has been handled")
        self.doNext(c)


class CharacterHandler(Handler):
    def __init__(self, next):
        Handler.__init__(self, next)

    def handle(self, c):
        if c.isalpha():
            print("Character has been handled")
        self.doNext(c)


class DigitHandler(Handler):
    def __init__(self, next):
        Handler.__init__(self, next)

    def handle(self, c):
        if c.isdigit():
            print("Digit has been handled")
        self.doNext(c)


handler = SymbolHandler(CharacterHandler(DigitHandler(None)))
handler.handle('A')
print("-----------------------------")
handler.handle('1')
print("====================================================")


class Handler(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abc.abstractmethod
    def check_range(self, request):
        """Compare passed value to predefined interval"""


class ConcreteHandler0(Handler):
    """Be simple and static"""

    @staticmethod
    def check_range(request):
        if 0 <= request < 10:
            print("request {} handled in handler 0".format(request))
            return True


class ConcreteHandler1(Handler):
    """ With it's own internal state"""
    start, end = 10, 20

    def check_range(self, request):
        if self.start <= request < self.end:
            print("request {} handled in handler 1".format(request))
            return True


class ConcreteHandler2(Handler):
    """ With helper methods."""

    def check_range(self, request):
        start, end = self.get_interval_from_db()
        if start <= request < end:
            print("request {} handled in handler 2".format(request))
            return True

    @staticmethod
    def get_interval_from_db():
        return (20, 30)


class FallbackHandler(Handler):
    @staticmethod
    def check_range(request):
        print("end of chain, no handler for {}".format(request))
        return False


def main():
    """
    >>> h0 = ConcreteHandler0()
    >>> h1 = ConcreteHandler1()
    >>> h2 = ConcreteHandler2(FallbackHandler())
    >>> h0.successor = h1
    >>> h1.successor = h2
    >>> requests = [2, 14, 22, 18, 3, 35, 20]
    >>> for request in requests:
    ...     h0.handle(request)
    request 2 handled in handler 0
    request 14 handled in handler 1
    request 22 handled in handler 2
    request 18 handled in handler 1
    request 3 handled in handler 0
    end of chain, no handler for 35
    request 20 handled in handler 2
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS, verbose=True)
