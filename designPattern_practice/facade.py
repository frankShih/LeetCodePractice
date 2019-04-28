'''
Provides a simpler unified interface to a complex system.

主要精神：簡化使用、隱藏依賴、降低耦合、有利分工合作

整合錯綜複雜的關係，提供較高級的介面。
Facade 參與者則是讓系統外埠看到較簡單的介面。
如此一來就不需要個別控制類別，只要把要求丟給"窗口"即可。

重點就在減少介面。太多的類別和方法，只會讓程式設計師猶豫該使用哪一個才對，
而且還得注意呼叫順序，容易弄錯。
所以不如把精神放在介面較少的 Facade 上，反而比較有效率。
'''


class ActionService:
    def doAction(self):
        some = Some()
        other = Other()
        # another = Another()
        # 作一些互動以產生結果
        print("Being busy in {} and {}.".format(some.work(), other.work()))


class Application:
    def __init__(self, service):
        self.service = service

    def doAction(self):
        self.service.doAction()


class Some():
    def work(self):
        return "~ some work ~"


class Other():
    def work(self):
        return "~ other work ~"


app = Application(ActionService())
app.doAction()

print("=======================================")


class CPU(object):
    """
    Simple CPU representation.
    """

    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print("Jumping to:", position)

    def execute(self):
        print("Executing.")


class Memory(object):
    """
    Simple memory representation.
    """

    def load(self, position, data):
        print("Loading from {0} data: '{1}'.".format(position, data))


class SolidStateDrive(object):
    """
    Simple solid state drive representation.
    """

    def read(self, lba, size):
        return "Some data from sector {0} with size {1}".format(lba, size)


class ComputerFacade(object):
    """
    Represents a facade for various computer parts.
    """

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


def main():
    """
    >>> computer_facade = ComputerFacade()
    >>> computer_facade.start()
    Freezing processor.
    Loading from 0x00 data: 'Some data from sector 100 with size 1024'.
    Jumping to: 0x00
    Executing.
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS, verbose=True)
