'''
Defines a base algorithm, deferring definition of exact steps to subclasses.

主要精神：父類別實作骨架，而將未實作抽象方法部份留待子類別來實作

在描述流程輸廓時，並沒有提及如何顯示訊息、
沒有提及如何取得使用者輸入等具體的作法，只是歸納出一些共同的流程步驟

從物件 建立的角度   <>  factory pattern
流程框架的角度      <>  template pattern
'''

# abc 套件，是為了要解決 Python 沒有 abstract class 的問題
# 透過抽象類別，可建立比起使用 hasattr() 更嚴格的 class interface 檢查
import random
from abc import ABCMeta, abstractmethod

class GuessGame(metaclass=ABCMeta):
    # 透過 abc.ABCMeta 這個 metaclass 實作抽象類別
    # 不用 metaclass，也可繼承 abc.ABC 這個 helper class 達到相同效果 
    #   class GuessGame(abc.ABC)
    # 抽象化 classmethod 以及 staticmethod: 只需要在 method decorator 後面加上 abstractmethod 即可
    # 抽象化 property: 同樣在 decorator 下面加上 abstractmethod 即可

    @abstractmethod
    def message(self, msg):
        pass

    @abstractmethod
    def guess(self):
        pass     

    def go(self):
        self.message(self.welcome)
        number = int(random.random() * 10)
        while True:
            guess = self.guess()
            if guess > number:
                self.message(self.bigger)
            elif guess < number:
                self.message(self.smaller)
            else:
                self.message(self.correct)
                break

class ConsoleGame(GuessGame):
    def __init__(self):
        self.welcome = "welcome to the guessing game"
        self.prompt = "please input a number："
        self.correct = "you got the answer"
        self.bigger = "your guess is larger than answer"
        self.smaller = "your guess is smaller than answer"
    
    def message(self, msg):
        print(msg)
    
    def guess(self):
        return int(input(self.prompt))

game = ConsoleGame()
print(isinstance(game, GuessGame), issubclass(ConsoleGame, GuessGame))  
game.go()
print("========================================================")


def get_text():
    return "plain-text"

def get_pdf():
    return "pdf"

def get_csv():
    return "csv"

def convert_to_text(data):
    print("[CONVERT]")
    return "{} as text".format(data)

def saver():
    print("[SAVE]")

def template_function(getter, converter=False, to_save=False):
    data = getter()
    print("Got `{}`".format(data))

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    if to_save:
        saver()

    print("`{}` was processed".format(data))

# 有兩個地方可以放doctest測試用例:
#   一個位置是模塊的最開頭
#   另一個位置是函數聲明語句的下一行
# 除此之外的其它地方不能放，放了也不會執行。

def main():
    """
    >>> template_function(get_text, to_save=True)
    Got `plain-text`
    Skip conversion
    [SAVE]
    `plain-text` was processed
    >>> template_function(get_pdf, converter=convert_to_text)
    Got `pdf`
    [CONVERT]
    `pdf as text` was processed
    >>> template_function(get_csv, to_save=True)
    Got `csv`
    Skip conversion
    [SAVE]
    `csv` was processed 123
    """
    # '>>>' 开头的行就是doctest测试用例。
    # 不带 '>>>' 的行就是测试用例的输出。
    # 如果实际运行的结果与期望的结果不一致，就标记为测试失败。

if __name__ == "__main__":
    # doctest 模塊會搜索像是 python 交互式會話中的代碼片段，
    # 然後嘗試執行並驗證結果
    import doctest
    doctest.testmod(verbose=True)