"""
Provides a way to encapsulate a group of individual factories.
(devide the products of factory into several group first)

in java: parentFactory(abstract), childFactories, (product interface), products
主要精神：composition(合成) - 多個零件工廠組裝出最後產品
"""


class beverage(object):
    def __init__(self, sugar, ice):
        self.sugar = sugar
        self.ice = ice

    def showIngredients(self):
        # print("")
        pass

class fruitTeaProducer(object):
    def __init__(self):
        self.tf = teaFactory()
        self.jf = juiceFactory()

    def getOrder(self, teaType, fruitType, sugar, ice):
        print("{} {} tea is composed of: ".format(fruitType, teaType))

        self.tf.getTea(sugar, ice, teaType).showIngredients()
        self.jf.getJuice(sugar, ice, fruitType).showIngredients()
        print("with sugar: {}, ice: {}".format(sugar, ice))

class teaFactory(object):
    def getTea(self, sugar, ice, order='green'):
        if order=='green':
            return greenTea(sugar, ice)
        elif order=='black':
            return blackTea(sugar, ice)

class greenTea(beverage):
    def __init__(self, sugar, ice):
        super().__init__(sugar, ice)

    def showIngredients(self):
        super().showIngredients()
        print("pure leaves")

class blackTea(beverage):
    def __init__(self, sugar, ice):
        super().__init__(sugar, ice)

    def showIngredients(self):
        super().showIngredients()
        print("leaves undergone withering and oxidation")


class juiceFactory(object):
    def getJuice(self, sugar, ice, order='apple'):
        if order=='apple':
            return appleJuice(sugar, ice)
        elif order=='orange':
            return orangeJuice(sugar, ice)

class appleJuice(beverage):
    def __init__(self, sugar, ice):
        super().__init__(sugar, ice)

    def showIngredients(self):
        super().showIngredients()
        print("apples")

class orangeJuice(beverage):
    def __init__(self, sugar, ice):
        super().__init__(sugar, ice)

    def showIngredients(self):
        super().showIngredients()
        print("oranges")


if __name__ == "__main__":
    ftp = fruitTeaProducer()
    ftp.getOrder("green", "apple", 7, 3)
