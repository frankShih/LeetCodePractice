'''
如果函式運用某個耗時的資源，可考慮將運算結果加以重用，這是效能調整上的考量。
方法之一是全域資源。然而，全域不是個好方式。
可以在函式中準備資源，建立 Closure 捕捉他，然後從函式中傳回 Closure ：
'''

# import math
# def prepare_factor(max):
#     # Creating a prime table is time-consuming.
#     primes = [i for i in range(2, max) if prime[i] == 1]

#     def factor(num):
#         while primes[i] ** 2 <= num:
#             if num % primes[i] == 0:
#                 list.append(primes[i])
#                 num //= primes[i]
#             else:
#                 i += 1

#     return factor

# factor = prepare_factor(100)
# print(factor(100)) # print [2, 2, 5, 5]


def dog():
    height = 40

    def profile():
        print("I'm a dog and my height is {}.".format(height))

    return profile


dog_profile = dog()
dog_profile()

'''
如果函式是物件，那麼就可以：
1. 被任何變數參考。
2. 不只被動地呼叫，還可以主動地傳入函式中，取代某個可重用流程模版中的演算法。
3. 建立 Closure 捕捉閒置變數（Free variable）並從函式中傳回。

不過，Python 的 Closure 有個重大的限制。沒辦法對閒置變數設值。
也就是說，在 Python 中，Closure 捕捉的閒置變數是唯讀的：
'''


def func():
    x = 10

    def getX():
        return x

    def setX(n):
        x = n   # 建立區域變數 x
    return (getX, setX)


getX, setX = func()
print(getX())  # 10

setX(20)
print(getX(), "\n")  # still 10

'''
如果呼叫 setX，上會在 setX 中建立區域變數 x，而不是將參數 n 指定給 func 的區域變數。
這就是為何最後會得到 10 的原因。

在 Python 3 中，可使用 global, nonlocal 關鍵字來指定變數的範圍，以避免情況：
'''


def func():
    x = 10

    def getX():
        return x

    def setX(n):
        nonlocal x
        x = n
    return (getX, setX)


getX, setX = func()
print(getX())  # 10

setX(20)
print(getX())  # 20

'''
被 closure 關進的 variable，是獨立的，僅依賴該 function scope，
對這個 function 的 captured variable 做操作，不會影響其他 function 的 captured variable
'''


def dog():
    height = 40

    def grow_up():
        nonlocal height
        height = height + 1

        def show_height():
            print(
                "Thanks for making me growing up. I'm now {} meters !!!!".format(height))

        return show_height

    return grow_up


if __name__ == "__main__":
    dog_1_grow_up = dog()
    dog_1_grow_up()
    dog_1_grow_up()
    dog_1_grow_up()()

    dog_2_grow_up = dog()
    dog_2_grow_up()()
