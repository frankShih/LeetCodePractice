import math
'''
當物件有 __get__（必要），以及 __set__、__delete__ (選擇性的)時，
它可以作為描述器（Descriptor）：
    def __get__(self, instance, owner)
    def __set__(self, instance, value)
    def __delete__(self, instance)
'''


class Descriptor:
    def __get__(self, instance, owner):
        print("get")
        print(self, instance, owner)

    def __set__(self, instance, value):
        print("set")
        print(self, instance, value)

    def __delete__(self, instance):
        print("delete")
        print(self, instance)


class Some:
    x = Descriptor()


s = Some()
print(s.x)
s.x = 10
print(s.x)
s.__dict__['x'] = 11
print(s.__dict__['x'])

del s.x


'''
特性(property)的尋找順序是：
    1. 在產生實例的類別 __dict__ 中尋找是否有相符的特性名稱。
        如果找到且是個描述器實例（具有 __get__），且具有 __set__ 或 __delete__，
        若為取值，則傳回__get__ 值，若為設值，則呼叫__set__（沒有則丟出 AttributeError），
        若為刪除特性，則呼叫__delete__()（沒有則丟出 AttributeError），
        如果描述器僅具有__get__()，則先進行第2步
    2. 在實例的 __dict__ 中尋找是否有相符的特性名稱
    3. 在產生實例的類別 __dict__ 中尋找是否有相符的特性名稱。如果不是描述器則直接傳回特性值。
        如果是描述器（此時一定是僅具有 __get__），則傳回 __get__()
    4. 如果實例有定義 __getattr__()，則看 __getattr__() 如何處理
    5. 如果實例沒有定義 __getattr__()，則丟出 AttributeError

'''


# property() 函式也可以使用修飾器語法，讓程式更為直覺


class Ball:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('必須是正數')
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @radius.deleter
    def radius(self):
        del self.__radius

    @property
    def volumn(self):
        return 4.0 / 3.0 * math.pi * self.__radius ** 3

    @volumn.setter
    def volumn(self, volumn):
        if volumn <= 0:
            raise ValueError('必須是正數')
        self.__radius = ((3.0 * volumn) / (4.0 * math.pi)) ** (1.0 / 3.0)


ball = Ball(10.0)
print(ball.volumn)
ball.volumn = 5000
print(ball.radius)


'''
Some 類別的 doSome 特性參考的物件，具有 __get__()，也就是說 doSome 特性實際上是個描述器，
在 Python 類別中定義的函式，實際上是個特性名稱參考至一個非資料描述器
'''
class Some:
    def doSome(self, arg):
        print(self, arg)

s = Some()
s.doSome(10)
Some.doSome(10, 20)






