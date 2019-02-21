from functools import wraps

'''
裝飾器本質上是一個Python 函數或類，
可以讓其他函數或類在不需要做任何代碼修改的前提下增加額外功能，
裝飾器的返回值也是一個函數/類對象。它經常用於有切面需求的場景，
比如：插入日誌、性能測試、事務處理、緩存、權限校驗等場景，
裝飾器是解決這類問題的絕佳設計。
可以抽離出大量與函數功能本身無關的雷同代碼到裝飾器中並繼續重用。
概括的講，裝飾器的作用就是為已經存在的對象添加額外的功能。
'''


print("*******function can be passed as param********")


def foo():
    print("foo")


def bar(func):
    func()


bar(foo)

print("*******using wrapping function********")
# create wrapping function for re-use


def use_logging(func):
    print("Log: %s is running" % func . __name__)
    func()


def foo():
    print('i am foo')


# break the struct of code
use_logging(foo)

print("********using decorator function with wrapper********")


def use_logging1(func):

    def wrapper():
        print("Log: %s is running" % func . __name__)
        return func()
        # 把foo當做參數傳遞進來時，執行func()就相當於執行foo()
    return wrapper


# 因為裝飾器use_logging(foo)返回的時函數對象wrapper，
# 這條語句相當於foo = wrapper
foo = use_logging1(foo)
foo()


@use_logging1   # @ 符號就是裝飾器的語法糖
def foo1():
    print("i am foo111")


foo1()

print("********using decorator function with warpper params********")


def use_logging2(func):
    def wrapper(* args,  ** kwargs):    # args是一個數組，kwargs一個字典

        print("Log: %s is running" % func . __name__)
        return func(* args,  ** kwargs)
    return wrapper


@use_logging2   #語法糖等價於  foo  =  use_logging2 ( foo )
def foo(name,  age=None,  height=None):
    print("I am %s , age %s , height %s " % (name,  age,  height))


foo('han', age=28, height=165)
print("********using decorator function with params********")

# 帶參數的裝飾器只需在原來不帶參數的裝飾器之上在最外層套一個函數，
# 該函數中定義參數，然後嵌套函數中引用參數即可實現。


def use_logging_level(level):
    def decorator(func):
        def wrapper(* args,  ** kwargs):
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


print("********using decorator class function********")

# 裝飾器不僅可以是函數，還可以是類，相比函數裝飾器，
# 類裝飾器具有靈活度大、高內聚、封裝性等優點。
# 使用類裝飾器主要依靠類的__call__方法，當使用'@'將裝飾器附加到函數上時，
# 就會調用此方法。


class Foo (object):
    def __init__(self, func):
        self . _func = func
        # self . _name  =  name

    def __call__(self):
        print('class decorator runing, ')
        self . _func()
        print('class decorator ending, ')


@Foo
def bar():
    print('bar')


bar()

print("********using decorator with functools.wraps function********")

# functools.wraps，wraps本身也是一個裝飾器，
# 它能把原函數的元信息拷貝到裝飾器裡面的func函數中，
# 使得裝飾器裡面的func函數也有和原函數foo一樣的元信息了。


def logged(func):
    @wraps(func)
    def with_logging(* args,  ** kwargs):
        print(func . __name__, kwargs)  # 輸出'f'
        print(func . __doc__, args)  # 輸出'does some math'
        return func(* args,  ** kwargs)
    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


f(10)
