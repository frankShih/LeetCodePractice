

'''
生成器是帶有 yield 的函數,而 generator iterator 則是 generator function 的
返回值, 即 generator 對象,如(elem for elem in [1, 2, 3]) 表達式,
稱為 generator expression, 實際使用與 generator 無異
'''

print("=========== generator iterator =============")
a = (elem for elem in [1, 2, 3])
print(a)

# 使得包含 yield 的函數成為一個返回迭代器的生成器，
# 而每條 yield 語句其實是往這個迭代器裡'push'一個元素

print("=========== fibonacci generator  =============")

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
generator 

由包含 yield 敘述的函式或產生器表達式(簡稱 genexp)所產生，
支援所有 iterator 的操作以及額外的 send()，客戶端可透過send()
與generator溝通、影響其內部狀態

iterator 的一種, 以更優雅的方式實現的 iterator.
可以像使用 iterator 一樣使用 generator, 當然除了定義.
定義一個 iterator,需要分別實現 __iter__()和 __next__(),
但 generator 只需要一個yield

generator 遇到 yield 後暫停, 確切點說是先返回 yield 表達式的值,再暫停.
當再次調用 next() 時,從先前暫停的地方開始執行,直到遇到下個 yield

將 yield 理解成中斷服務子程序的断点,每次對 generator 調用 next() 時,
函數內部執行到 ”斷點” yield, 返回結果, 並保存上下文環境, ”中斷” 返回
'''

print("=========== generator expression =============")

def gen():
    while True:
        s = yield
        print(s)


g = gen()
next(g)
g.send("kissg")

'''
generator 第2種調用方法(恢復執行),通過 send(value) 將 value 
作為 yield 表達式的當前值,用該值對其他變量進行賦值.
當調用 send(value) 時, generator 正由於 yield 被暫停.
此時 send(value) 傳入值作為 yield 的值, 再遇到 yield,暫停返回.

調用 send(value) 時要注意,要確保 generator 是在 yield 處被暫停,
如此才能向 yield 表達式傳值, 可通過 next() 或 send(None) 
使 generator 執行到 yield

*** 以 yield 分離代碼進行解讀 ***
'''


def echo(value=None):
    while 1:
        print("before yield: ", value)

        value = (yield value)
        print("The value is", value)
        if value:
            print("plus one")
            value += 1


g = echo(1)
print(111, next(g))
print(222, g.send(2))
print(333, g.send(5))
print(444, next(g))

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
