'''
Creates new object instances by cloning prototype.

主要精神： 不是利用類別產生物件個體，而是從一個物件個體產生出另外一個新物件個體

make it easier to derive new kinds of objects,
when class have only a few different combinations of state, 
and when instantiation is expensive.

1. 種類過多無法整成類別時
2. 不容易利用類別產生物件個體時: 該物件個體的產生過程太複雜
'''

class Prototype(object):
    value = 'default'

    def clone(self, **attrs):   # vary-size "key-val" variables
        """Clone a prototype and update inner attributes dictionary"""
        # Python in Practice, Mark Summerfield
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])



import copy

class Wheel:
    def clone(self):
        return copy.deepcopy(self)

class Car:
    def __init__(self):
        self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
    def clone(self):
        return copy.deepcopy(self)

class Cars:
    def __init__(self):
        self.prototypes = {}
    def addPrototype(self, brand, car):
        self.prototypes[brand] = car
    def getPrototype(self, brand):
        return self.prototypes[brand].clone()


if __name__ == '__main__':
    main()

    bmw = Car()
    benz = Car()
    cars = Cars()
    cars.addPrototype("BMW", bmw)
    cars.addPrototype("BENZ", benz)
    bmwPrototype = cars.getPrototype("BMW")
    # 避免子類化為物件創建者（object creator）