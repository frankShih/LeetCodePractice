"""
Creates objects without having to specify the exact class

Provide an interface, keep implementation away from the caller
主要精神：inheritance(繼承)

簡單工廠管理物件的創造，如果 client 要取得物件，只要給簡單工廠正確的參數就可以。
[尚未將繼承觀念引入，純粹隔離 consumer & producer]
"""

class idCard(object):
    def __init__(self, name, num):
        self.name = name
        self.id = num

    def showInfo(self):
        print("this is {}, id: {}".format(self.name, self.id))


class idCardNewFormat(object):
    def __init__(self, name, num):
        self.name = name
        self.id = num

    def showInfo(self):
        print("{} from new devision, id: {}".format(self.name, self.id))


class idCardProvider(object):
    counter = 0
    def getCard(self, name):
        card = idCard(name, self.counter)
        self.counter += 1
        return card

''' simple factory method
the [if/else] style
'''
class idCardSimpleFactory(object):

    def __init__(self):
        self.counter = 0

    def getCard(self, name, format='origin'):
        # may be non-related objects
        if format == 'origin':
            card = idCard(name, self.counter)
        elif format == 'new':
            card = idCardNewFormat(name, self.counter)

        self.counter += 1
        return card


''' factory method (inhertance)
工廠方法模式定義了一個建立物件的介面，但由子類決定要實例化的類別為何。
工廠方法讓類別把 實例化 的動作推遲到了子類。
'''
class idCardType1(idCard):
    def __init__(self, name, num):
        super().__init__(name, num)
    def showInfo(self):
        super().showInfo()
        print("this is type one ~~")

class idCardType2(idCard):
    def __init__(self, name, num):
        super().__init__(name, num)
    def showInfo(self):
        super().showInfo()
        print("this is type two ~~")

class idCardFactory(object):
    def __init__(self):
        self.counter = 0

    def getCard(self, name, cType=1):
        # implement method in super-class
        # user only need to know how super-class look like
        if cType == 1:
            card = idCardType1(name, self.counter)
        elif cType == 2:
            card = idCardType2(name, self.counter)

        self.counter += 1
        return card


if __name__ == "__main__":
    provider = idCardProvider()
    card1 = provider.getCard("haha")
    card2 = provider.getCard("hihi")

    card1.showInfo()
    card2.showInfo()

    factory = idCardSimpleFactory()
    card1 = factory.getCard("hoho", "new")
    card2 = factory.getCard("hehe")
    card1.showInfo()
    card2.showInfo()

    factory = idCardFactory()
    card1 = factory.getCard("hoho", 1)
    card2 = factory.getCard("hehe", 2)
    card1.showInfo()
    card2.showInfo()
