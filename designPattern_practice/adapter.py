'''
An interface of class(es) to be used by others   

主要精神：設計 wrapper，將既有內容包裝之後，重新再利用

既有內容無法直接利用時，需要先轉換型態後再使用。
具有填平"既有內容"和"需要結果"兩者間的落差就是 Adapter Pattern

版本更新時常碰到的問題是版本的相容性。
利用 Adapter Pattern 可讓新舊版本共存，維護更容易。
'''

class Adaptee:
    def doAction(self):
        print('Adaptee called')
 
class Adapter:
    def __init__(self, adaptee):    # or using inhertance "繼承"
        self.adaptee = adaptee  # 或使用 "委讓"
 
    def request(self):
        print('Adapter called & do something')
        self.adaptee.doAction()
 
client = Adapter(Adaptee())
client.request()

print('=====================================')


class Dog(object):
    def __init__(self):
        self.name = "Dog"

    # implementation of method still in class, hence not visitor pattern 
    def bark(self): 
        return "woof!"

class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"

class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)

'''
class 或 instance 擁有 __dict__ 字典物件，其中記錄著所擁有的 property
如果 instance 的__dict__ 中沒有，則到產生 class.__dict__ 中尋找

這也說明了，為什麼實例方法的第一個參數會綁定至實例
類別中所定義的函式，就是類別的特性，在類別的 __dict__ 可找到該名稱。
實例方法 1st 參數 self 綁定實例，透過 self.x 設定特性值 (self.__dict__中添增 property)

Python 可動態為類別添加屬性，即使是未添加屬性前就已建立的物件
如果在實例上呼叫某個方法，而實例上沒有該綁定方法時（@staticmethod / @classmethod 修飾）
則會試著去 class.__dict__ 尋找，並以 class 呼叫方式來執行函式
如果類別 __dict__ 仍沒有，則會呼叫 __getattr__()，
如果沒有定義 __getattr__()，則會 AttributeError

類別中的特性名稱是以__開頭，則該名稱會被加工處理:
實例若以 __name 名稱，則會自動轉換為「_類別名__name」儲存在實例的__dict__中，
以 __ 開頭的變數名稱，Python 沒有真正阻止你存取它，但提示不希望你直接存取 (private style)
'''

class Adapter(object):
    # Adapts an object by replacing methods.
    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)   # add key-val pairs

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__

    def show_info(self):    # adaptive function
        print("A {0} goes {1}".format(self.name, self.make_noise()))

def main():
    """
    >>> objects = []
    >>> dog = Dog()
    >>> print(dog.__dict__)
    {'name': 'Dog'}
    >>> objects.append(Adapter(dog, make_noise=dog.bark))
    >>> objects[0].__dict__['obj'], objects[0].__dict__['make_noise']
    (<...Dog object at 0x...>, <bound method Dog.bark of <...Dog object at 0x...>>)
    >>> print(objects[0].original_dict())
    {'name': 'Dog'}
    >>> cat = Cat()
    >>> objects.append(Adapter(cat, make_noise=cat.meow))
    >>> car = Car()
    >>> objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))
    >>> for obj in objects:
    ...    obj.show_info()
    A Dog goes woof!
    A Cat goes meow!
    A Car goes vroom!!!
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS, verbose=True)

