# -*- coding: utf-8 -*-

from contextlib import contextmanager
'''
資源的管理在程式設計上是個很常見的問題，例如管理開啟的檔案、
網路 socket 與各種鎖定（locks）等，主要問題在於確保這些開啟的資源
在使用之後，有確實關閉（釋放），如果忘記就會造成效能問題，甚至錯誤，
除了關閉之外，有些特殊的資源在使用後，必須進行後續的清理動作，
這些也都是資源管理上需要注意的。

Python 語言提供 with 語法，可更容易管理這些開啟的資源，
Python 會自動進行資源建立、清理與回收，程式設計者在使用各種資源時更為方便。
'''


# 傳統上若要開啟一個檔案，我們會這樣寫：

# 開啟檔案
f = open('./file.txt', 'r')

try:
    for line in f:
        print(line)
except Exception as e:
    print('Exception1: ', e)
finally:
    # 關閉檔案
    f.close()


# 這種狀況我們就可以改用 with 的寫法：
try:
    with open('./file.txt', 'w') as f:
        f.write('Hello, world!')
except Exception as e:
    print('Exception2: ', e)
    # get line number and error message
    with open('./file.txt', 'a') as f:
        f.write('an error message')

'''
自行建立 context manager，定義好類別的 __enter__ , __exit__ 函數即可，
with 開始時，會執行 __enter__ 函數，傳回配給的資源（例如開啟的檔案），
with 範圍結束時，會自動呼叫 __exit__ 釋放資源（例如關閉檔案）。
'''


class TraceBlock(object):
    def message(self, arg):
        print('running' + arg)

    def __enter__(self):
        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception! ' + str(exc_type))
            return False  # Propagate


with TraceBlock() as action:
    action.message('test1')
    print('reached')

    with TraceBlock() as action:
        action.message('test2')
        raise TypeError
        print('not reached')


'''
除了使用類別外，也可使用 contextlib 模組的 decorator 來產生
@contextmanager 只是減少了代碼量

@contextmanager 不負責資源“獲取/清理”（開發者自己實現）
“獲取”需定義在 yield 語句之前，“清理”需定義 yield 語句之後
'''


@contextmanager
def open_file(name, mode):
    # 配給資源（開啟檔案）
    f = open(name, mode)
    yield f
    # 回收資源（關閉檔案）
    f.close()


with open_file('file.txt', 'w') as f:
    f.write("Hello, world.")
