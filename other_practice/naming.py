# -*- coding: utf-8 -*-

'''
python並沒有所謂的private
但可以在member的前面加上一個底線 當作一個軟性的private

也可以在member前面加上雙底線 這樣會產生name mangling的效果
但這樣也不能完全達到禁止存取

'''
class Parent:
    __name_mangling = "__name_mangling"
    _name = "_name"

    def show(self):
        print(self.__name_mangling)
        print(self._name)


p = Parent()
print(dir(p))
p.show()  # __name_mangling  # _name

try:
    print(p.__name_mangling)
except AttributeError as e:
    print("AttributeError: {}".format(e))


print(p._Parent__name_mangling)  # __name_mangling
''' 在雙底線的member前面加上_className來存取 但危險 非常不建議使用'''
print(p._name)  # _name
''' 單底線的member 可自由存取 但仍然不應該這樣做'''


class Child(Parent):
    __name_mangling = "child's __name_mangling"
    _name = "child's _name"

    def child_show(self):
        print(self.__name_mangling)
        print(self._name)

'''
name mangling 效果會在繼承時產生特別的效果
除非我們想要達到這樣的效果
不然一般的情況不太需用到name mangling
'''
c = Child()
print(dir(c))
c.show() #__name_mangling (from parent)  #child's _name (override)
c.child_show() #child's __name_mangling #child's _name

'''
使用from xxxx import *的時候不會import含有單底線的function 以避免汙染環境
若想取用含底線的資源 import必須指明from underscore import __underscore_foo

不論如何「from xxxx import *」都不建議使用 因為很容易缺染環境
一般還是建議使用import xxx 然後使用xxx.yyy的方式來取用資源
或是使用from xxx import yyy的方式 就可以直接以yyy的方式來取用資源
'''



