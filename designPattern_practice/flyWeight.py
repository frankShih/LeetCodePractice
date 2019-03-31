'''
Minimizes memory usage by sharing similar objects

主要精神：以 pool 統一管控與 context 無關之 objects 的存取

當想要節省記憶體空間的時候使用。
儘量共用物件個體，不做無謂的new，或使用 weak reference 自動回收
'''

'''
__init__() 定義物件建立後初始化的流程，傳入__init__()的引數，
並不是作為建構物件之用，而是作為初始物件之用。

實際上要決定如何建構物件，必須定義__new__()
__new__() 的第一個參數傳入類別本身，之後可接任意參數作為建構物件之用。

__new__() 可以傳回物件，如果傳回的物件是第一個參數的類別實例，
則會執行__init__()，而__init__()的第一個參數綁定所傳回的物件。
如果沒有傳回第一個參數的類別實例（傳回別的實例或None），
則不會執行__init__()方法（即使有定義）。
應用的例子，就是實作 Singleton 模式。

如果要定義物件被垃圾收集（Garbage collection）時，
所要進行的資源清除動作，則可以定義__del__()方法

Python 習慣用 cls 當作指向 class 的變數名稱、
並用 self 當作指向 instance 的變數名稱。

有時候難免會有 "讓這個類別的物件個體只產生一個" 的需要，
像是用程式來表現在程式中絕對是獨一無二的某個部份。
 >1 物件個體時，物件個體彼此間的影響，可能會發展出乎意料的 bug
'''

class Singleton:
    __single = None
    def __new__(cls):
        if not Singleton.__single:
            Singleton.__single = super().__new__(cls)
        return Singleton.__single
        
    def doSomething(self):
        print("do something...XD")
    
    def __init__(self):
        print('__init__')
    
    def __del__(self):
        print('__del__')    

singleton1 = Singleton()
singleton1.doSomething()  # do something...XD

singleton2 = Singleton()
singleton2.doSomething()  # do something...XD

print(id(singleton1), id(singleton2), singleton1 is singleton2)  # True


'''
物件導向語言中的「class」是用來「描述如何建立 object」的程式碼；
寫 class 就是為了建立 object。然而在 Python 中：
    連 class 本身也是 object
    class 是 meta class 的 instance。
    meta class 是 class 的 class。

當你一寫下 class 關鍵字 ，Python 會執行它，並建立一個 class object

這個 class object 並不是 class instance，而是 class 自己本身。
這個 class object 的功能就是建立自己的 instance object。


type() 內建函數極度詭異，當塞三個參數時，功能會變成建立 class object
    type(name, bases, dict) 分別對應到 class attributes 中的：
        name 變成 __name__，就是 class 的名稱
        bases 變成 __bases__，就是該 class 要繼承自哪些 base class
        dict 變成 __dict__ ，就是該 class 所有的 member

這兩種寫法的意義是完全相同的 - 
class Hello:   # 預設繼承自 object
    pass

DynamicHello = type("DynamicHello", (), {})

Python 裡面所有的 class 都是 type 的 instance。

Metaclass
    metaclass 是 class 的 class，也就是說:
    object 是 class 的 instance
    class 是 metaclass 的 instance

type
    type 是 Python 中的 metaclass:
    type 本身也是一個 class
    type 本身的 metaclass 就是他自己

要寫一個 metaclass 的話，就繼承 type

假設我們定義了一個 class 叫 Hello
__call__    定義了當 Hello 後面被加上小括號、當作 function 來呼叫時的行為。
            預設行為是依序呼叫 __new__() 跟 __init__()
__new__     定義了 Hello 如何實體化，最後會回傳一個實體 object。
__init__    定義了 Hello 實體化後，其實體 object 如何初始化
            （例如 member variable 定義之類的，這是大家最熟悉的部份）。
'''


import weakref

'''
class FlyweightMeta(type):
    def __new__(mcs, name, parents, dct):
        """
        Set up object pool
        :param name: class name
        :param parents: class parents
        :param dct: dict: includes class attributes, class methods,
        static methods, etc
        :return: new class
        """
        dct['pool'] = weakref.WeakValueDictionary()
        return super(FlyweightMeta, mcs).__new__(mcs, name, parents, dct)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
        """
        Serialize input parameters to a key.
        Simple implementation is just to serialize it as a string
        """
        args_list = list(map(str, args))
        args_list.extend([str(kwargs), cls.__name__])
        key = ''.join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        key = FlyweightMeta._serialize_params(cls, *args, **kwargs)
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if instance is None:
            instance = super(FlyweightMeta, cls).__call__(*args, **kwargs)
            pool[key] = instance
        return instance
'''

class Card(object):
    _CardPool = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):  # cls - class object
        obj = Card._CardPool.get(value + suit)
        if not obj:
            obj = object.__new__(Card)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    # using 'new' to replace init
    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit

    def __repr__(self): # class instance object
        return "<Card: %s%s>" % (self.value, self.suit)


# class Card2(metaclass=FlyweightMeta):
#     def __init__(self, *args, **kwargs):
#         # print('Init {}: {}'.format(self.__class__, (args, kwargs)))
#         pass


if __name__ == '__main__':
    # comment __new__ and uncomment __init__ to see the difference
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2, c1 is c2)
    print(id(c1), id(c2))

    c1.temp = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))
    c1 = c2 = c3 = None     # remove instance from pool & reassign
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))

    # Tests with metaclass
    # instances_pool = getattr(Card2, 'pool')
    # cm1 = Card2('10', 'h', a=1)
    # cm2 = Card2('10', 'h', a=1)
    # cm3 = Card2('10', 'h', a=2)

    # assert (cm1 == cm2) and (cm1 != cm3)
    # assert (cm1 is cm2) and (cm1 is not cm3)
    # assert len(instances_pool) == 2

    # del cm1
    # assert len(instances_pool) == 2

    # del cm2
    # assert len(instances_pool) == 1

    # del cm3
    # assert len(instances_pool) == 0

