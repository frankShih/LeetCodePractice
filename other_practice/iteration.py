# -*- coding: utf-8 -*-

from collections import Iterable
'''
迭代通常通過for ... in ...完成, 只要是可迭代对象(iterable),都能迭代

1. iterable 
實現 __iter__() 的對象. 更確切的說是container.__iter__(),
返回一個 iterator 對象, 一些 iterable 將所有值都存儲在內存中,比如 list,
而另一些並不是這樣, 比如 iterator

是容器本身，將 iterable 傳進 iter() 得到一個 iterator
沒有狀態的，每次對 Iterable 調用 iter() 會得到新的迭代器。

2. iterator 
實現 iterator.__iter__() 和 iterator.__next__() 的對象.
iterator.__iter__() 返回 iterator 本身. 實現 for ... in ...語句.

而 iterator.__next__() 是 iterator 區別 iterable 的關鍵,
允許顯式地獲取元素.當調用 next() 時,實際上產生了2個操作:
    I.更新 iterator 狀態,令其指向後一項, 以便下次調用
    II. 返回當前結果

透過 next() 不斷取出下個元素，尾端丟出 StopIteration
有狀態的，只能遍歷一次，是 “消費型”，不可 “二次消費”。

Python2 中 range() 返回 list，Python3 range 已經使用 xrange 替換，
返回的是一個Iterable。
'''


from collections import Iterable, Iterator
a = [1, 2, 3]   # list 是 iterable
b = iter(a)   # 得到iterator, invoke __iter__()
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(b, Iterable))
print(isinstance(b, Iterator))
# iterator 是 iterable, 但 iterable 不一定是 iterator

# iterator 是消耗型的,用一次少一次.
c = list(b)
print(c)
d = list(b)
print(d)


if b:
    print(111)
if b == None:   # 空的 iterator 不等于 None.
    print(222)

e = iter(a)
print(next(e))  # next() invoke __next__()
print(next(e))


'''
可迭代對象（Iterable）
通常是個容器、iterable 實作 __iter__ 回傳一個參考到此容器內部的 iterator

1. anything that can be looped over (i.e. string or file)
2. anything that can appear on the right-side of a for-loop:  
    for x in iterable: ...
3. anything you can call with iter() that will return an ITERATOR:  
    iter(obj)
4. object that defines __iter__ that returns a ITERATOR, 
    (it may have a __getitem__ suitable for indexed lookup)
'''


# 使用 hasattr() 判斷對像是否可迭代
hasattr((), '__iter__')
hasattr([], '__iter__')
hasattr({}, '__iter__')
hasattr(123, '__iter__')
hasattr('abc', '__iter__')
hasattr('abc', '__getitem__')

# 也可使用 isinstance() 進行判斷

isinstance((), Iterable)        # 元组
isinstance([], Iterable)        # 列表
isinstance({}, Iterable)        # 字典
isinstance('abc', Iterable)     # 字符串
isinstance(100, Iterable)       # 数字


'''
迭代器 ITERATOR
iterator pattern 在 Python 中的實作，為序列或容器型態提供相同的介面
讓客戶端 iterate over 容器內元素，iterator 實作__next__ 與 __iter__，
別供 next() 與 iter() 呼叫，每個 iterator 同時也是一個iterable

1. with state that remembers where it is during iteration
2. with a __next__ method that:
    returns next value in the iteration
    updates the state to point at the next value
    signals when it is done by raising StopIteration
3. is self-iterable (has an __iter__ that returns self).

Iterator 也要求實現 __iter__()，因為很多地方接收的參數是 Iterable，
如果 Iterator 都是 Iterable，那麼這些地方都可以無障礙地使用 Iterator
'''
