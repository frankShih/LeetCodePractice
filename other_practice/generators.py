'''
迭代通常通過for ... in ...完成,只要是可迭代对象(iterable),都能迭代

1. iterable 是實現 __iter__() 的對象.更確切的說是container.__iter__(),
返回一個 iterator 對象,一些 iterable 將所有值都存儲在內存中,比如 list,
而另一些並不是這樣, 比如 iterator

2. iterator 是實現 iterator.__iter__() 和 iterator.__next__() 的對象.
iterator.__iter__() 方法返回 iterator 本身. 實現了for ... in ...語句.
而iterator.__next__() 是 iterator 區別 iterable 的關鍵,
它允許顯式地獲取一個元素.當調用 next() 時,實際上產生了2個操作:
    I.更新iterator狀態,令其指向後一項,以便下一次調用
    II. 返回當前結果

'''


from collections import Iterable, Iterator
a = [1, 2, 3]   # 众所周知,list是一个iterable
b = iter(a)   # 通过iter()方法,得到iterator,iter()实际上调用了__iter__(),此后不再多说
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(b, Iterable))
print(isinstance(b, Iterator))
# 可见,itertor一定是iterable,但iterable不一定是itertor

# iterator是消耗型的,用一次少一次.对iterator进行变量,iterator就空了!
c = list(b)
print(c)
d = list(b)
print(d)

# 空的iterator并不等于None.
if b:
    print(111)
if b == None:
    print(222)


# 再来感受一下next()
e = iter(a)
print(next(e))  # next()实际调用了__next__()方法,此后不再多说
print(next(e))


'''
對 iterable 用 for ... in ... 進行迭代時,實際是先通過調用 iter() 得到
iterator, 假設叫做 X. 然後循環地調用 X.next() 取得每一次的值,
直到 iterator 為空, 返回的 StopIteration 作為循環結束的標誌.
for ... in ... 自動處理 StopIteration 異常, 避免了拋出異常使程序中斷

生成器是帶有 yield 的函數,而generator iterator 則是 generator function的
返回值, 即 generator 對象,如(elem for elem in [1, 2, 3])的表達式,
稱為 generator expression,實際使用與 generator 無異

'''

a = (elem for elem in [1, 2, 3])
print(a)

# 使得包含yield的函數成為一個返回迭代器的生成器，而每條yield語句其實是往這個迭代器裡'push'一個元素 ,這個元素就是yield後面緊跟的表達式的值
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


print(fib)

b = fib()
print(b)
print(next(b))
print(next(b))

'''
generator 是 iterator 的一種,以更優雅的方式實現的iterator.
可以像使用 iterator 一樣使用 generator, 當然除了定義.
定義一個 iterator,需要分別實現 __iter__()和 __next__(),
但 generator 只需要一個yield

generator 遇到 yield 之後暫停,確切點說是先返回 yield 表達式的值,再暫停的.
當再次調用 next() 時,從先前暫停的地方開始執行,直到遇到下個 yield

將 yield 理解成中斷服務子程序的断点,每次對 generator 調用next()時,
函數內部代碼執行到”斷點” yield, 然後返回這部分的結果,
並保存上下文環境,”中斷”返回
'''


def gen():
    while True:
        s = yield
        print(s)


g = gen()
next(g)
g.send("kissg")

'''
generator 第2種調用方法(恢復執行),通過send(value)將value作為yield
表達式的當前值,用該值再對其他變量進行賦值.當調用send(value)時,
generator 正由於 yield 被暫停.此時 send(value)傳入值作為 yield
表達式的值,循環再遇到yield,暫停返回.

調用send(value)時要注意,要確保 generator 是在 yield處被暫停了,
如此才能向 yield 表達式傳值,
可通過 next() 或 send(None) 使 generator執行到 yield
*** 以yield分離代碼進行解讀 ***
'''


def echo(value=None):
    while 1:
        value = (yield value)
        print("The value is", value)
        if value:
            value += 1


g = echo(1)
print(next(g))
print(g.send(2))
print(g.send(5))
print(next(g))

'''
Saving memory space
Iterators don’t compute the value of each item when instantiated.
They only compute it when you ask for it. (lazy evaluation)
'''


def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


class Primes:
    def __init__(self, max):
        self.max = max
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            return self.number
        else:
            return self.__next__()


primes = Primes(10)
print(primes)
for x in primes:
    print(x)

#  generator functions create iterators in a more simple fashion
def Primes(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number


primes = Primes(10)
print(primes)
for x in primes:
    print(x)

# list comprehension equivalent of generators.
# It works exactly in the same way as a list comprehension,
# but the expression is surrounded with () as opposed to [].
primes = (i for i in range(2, 10) if check_prime(i))
print(primes)
for x in primes:
    print(x)

