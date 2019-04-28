from functools import wraps

'''
裝飾器
本質上是個Python 函數或類，
可讓其他函數或類在不需要做任何代碼修改的前提下增加額外功能，
返回值也是一個函數/類對象。

經常用於有切面需求(將功能切分成獨立區塊)的場景，如：日誌、
性能測試、事務處理、緩存、權限校驗等，裝飾器是這類問題的絕佳設計。

可以抽離出大量與函數功能本身無關的雷同代碼到裝飾器中並繼續重用。
概括的講，裝飾器的作用就是為已存在的對象添加額外功能。
'''

print("\n******* using wrapping function ********")
# create wrapping function for re-use


def use_logging(func):
    print("Log: %s is running" % func . __name__)
    func()


def foo():
    print('i am foo')


# break the struct of code
use_logging(foo)

print("\n******** using decorator function with wrapper (Syntactic sugar) ********")


def use_logging1(func):

    def wrapper():  # closure function (any name)
        print("Log: %s is running" % func . __name__)
        return func()
        # 把 foo 當做參數傳遞進來時，執行 func() 就相當於執行 foo()

    return wrapper


foo = use_logging1(foo)
foo()


@use_logging1   # @ 符號就是裝飾器的語法糖
def foo1():
    print("i am foo111")


# 省一句 function wrapping assignment
foo1()

print("\n******** using decorator function to pass params ********")

'''
# only one param
def  wrapper(name): 
        logging . warn ( " %s is running"  %  func . __name__ ) 
        return  func ( name ) 
    return  wrapper

# unknown number of params
def  wrapper(*args): 
        logging . warn ( " %s is running"  %  func . __name__ ) 
        return  func ( * args ) 
    return  wrapper    
'''


def use_logging2(func):
    # key word params -> using **kwargs
    def wrapper(*args,  **kwargs):    # args 是一個數組，kwargs 一個字典
        print("Log: %s is running" % func . __name__)
        return func(*args,  **kwargs)

    return wrapper


@use_logging2  # 語法糖等價於  foo  =  use_logging2 ( foo )
def foo(name,  age=None,  height=None):
    print("I am %s , age %s , height %s " % (name,  age,  height))


foo('han', age=28, height=165)


print("\n******** using decorator function with params ********")

# 帶參數的裝飾器只需在原來不帶參數的裝飾器之上在最外層套一個函數，
# 該函數中定義參數，然後嵌套函數中引用參數即可實現。


def use_logging_level(level):   # wrapper param
    def decorator(func):    # wrapped funciton
        def wrapper(*args,  **kwargs):  # wrapped funciton param
            if level == "warn":
                print("Log-warn: %s is running" % func . __name__)
            elif level == "info":
                print("Log-info: %s is running" % func .__name__)
            return func(* args)

        return wrapper

    return decorator


@use_logging_level(level="warn")
def foo(name='foo'):
    print("i am %s " % name)


foo()


print("\n******** using decorator class function ********")

# 裝飾器還可以是類，類裝飾器具有靈活度大、高內聚、封裝性等優點。
# 類裝飾器主要依靠 __call__，使用 '@' 附加到函數上時，會調用此方法。


class Foo (object):
    def __init__(self, func):
        self._func = func
        # self . _name  =  name

    def __call__(self):
        print('class decorator runing, ')
        self._func()
        print('class decorator ending, ')


@Foo
def bar():
    print('bar')


bar()

print("\n******** using decorator with functools.wraps ********")

'''
# not true in python 3
# 裝飾器複用代碼，但是有個缺點就是原函數的元信息不見了，
# 比如函數的 docstring、 __name__、 參數列表


def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__, kwargs)
        print(func.__doc__, args)
        return func(*args, **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


f(1)
'''

# functools.wraps，wraps 本身也是個裝飾器，
# 能把原函數的元信息拷貝到裝飾器裡面的 func 函數，
# 使裝飾器裡 func() 和原函數 foo() 有一樣的元信息。


def logged(func):
    @wraps(func)
    def with_logging(*args,  **kwargs):
        print(func.__name__, kwargs)
        print(func.__doc__, args)
        return func(*args,  **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


f(10)
