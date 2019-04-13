'''
decouples the creation of a complex object and its representation,
so that the same process can be reused to build objects

主要精神：整個物件的產生過程封裝起來

如果物件是由個別組件（Component）組成，個別組件建立非常複雜，
但說明如何運用組件建立物件非常簡單
希望將"建立複雜組件"與"運用組件方式"分離，則可使用 Builder 模式。

=> 建立個 builder，將各組件複雜的實作封裝。由 director 調用並組出最終的物件
Builder 著重在隱藏物件生成的步驟；而 Abstract Factory 著重在管理有關聯性的物件
'''

# Abstract Building
class Building(object):
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


# Concrete Buildings
class House(Building):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big'


class Flat(Building):
    def build_floor(self):
        self.floor = 'More than One'

    def build_size(self):
        self.size = 'Small'


# In some very complex cases, it might be desirable to pull out the building
# logic into another function (or a method on another class), rather than being
# in the base class '__init__'. (This leaves you in the strange situation where
# a concrete class does not have a useful constructor)


class ComplexBuilding(object):
    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        print("some complex logics in constructing object.floor")
        self.floor = 'One'

    def build_size(self):
        print("some complex logics in constructing object.size")
        self.size = 'Big and fancy'


def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building


# Client
if __name__ == "__main__":
    house = House()
    print(house)
    flat = Flat()
    print(flat)

    # Using an external constructor function:
    complex_house = construct_building(ComplexHouse)
    print(complex_house)


'''
str()   '可讀性'較高，是給開發者閱讀對象中'有用資訊'的字串
repr()  全名是 representation，其字串是給 python 直譯器看的，
        這個字串會顯示'明確且詳盡的資訊'
In python3 shell:
>>> class Test():
...     def __init__(self):
...             pass
...     def __repr__(self):
...             return "the repr"
...     def __str__(self):
...             return "the str"
... 
>>> a = Test()
>>> a
the repr
>>> print(a)
the str
'''



