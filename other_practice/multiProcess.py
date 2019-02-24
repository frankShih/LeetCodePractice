from multiprocessing import Value as mpV
from multiprocessing import Queue as mpQ
from multiprocessing import Pool
import traceback
import os
from multiprocessing import Process, Lock, freeze_support, set_start_method
'''
功能：並行處理
因 Global Interpreter Lock (GIL, CPython)，multithread 需用
multiprocess 取代，

問題的癥結在,要想利用多核系統，Python 必須支持多線程運行。
作為解釋型語言，Python的解釋器必須既安全又高效。多線程編程會遇到問題。
解釋器要避免在不同線程操作內部共享的數據。同時還要保證在管理用戶線程時
保證總是有最大化的計算資源。

不同線程同時訪問時，數據的保護機制是怎樣的呢？答案是解釋器全局鎖。
這是一個加在解釋器上的全局（從解釋器的角度）鎖（從互斥角度看）。

有了GIL這超級大鎖，而當越來越多的代碼庫開發者接受這種設定後，
開始依賴這種特性（默認python內部對像是thread-safe，無需在實現時
考慮額外的內存鎖和同步操作）。

這種方式很安全，但是它有隱含的意思：對Python程序，不管有多少的處理器，
任何時候都只有一個線程在執行。

”為什麼多線程Python程序運行得比單線程的時還要慢？“ （假設該程序是可並行的）
Python的專家們精心製作了一個標準答案：”不要使用多線程，請使用多進程。“

由於Python解釋器的設計，使用多線程以提高性能是個困難的任務。最壞的情況下，
它將會降低（有時很明顯）程序的運行速度


'''

from threading import Thread
import time


def my_counter():
    i = 0
    for _ in range(1000000):
        i = i + 1
    return True


thread_array = {}


def f(q, lock, i):
    print('{:2d} Stop'.format(i))
    # 暫停 1s，這邊是為了看出其他 child process Stop 的效果，才暫停的
    time.sleep(1)
    # block 直到上一個 child process 解鎖
    lock.acquire()
    try:
        print('{:2d} Start'.format(i))
        q.put(i)
    finally:
        # 必做解鎖，不然會影響到下一個 child process
        lock.release()


# 多個 child process 建議用法
# Value/Array - shared memory for multi-process


def job(v, num, l):
    l.acquire()
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()


def multicore():    #lock shared memory
    l = Lock()
    v = mpV('i', 0)
    p1 = Process(target=job, args=(v, 1, l))
    p2 = Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def handle_error(e):
    '''處理 child process 的錯誤，不然 code 寫錯時，不會回報任何錯誤'''
    traceback.print_exception(type(e), e, e.__traceback__)


def long_time_task(name):
    print('任務 {} ({}) 開始'.format(name, os.getpid()))
    start = time.time()
    time.sleep(1)
    end = time.time()
    print('任務 {} 執行 {:0.2f} seconds.'.format(name, (end - start)))
    return name


# 因 window spawn 的緣故, 必須在 '__main__' 之內執行
if __name__ == '__main__':
    # 順序執行的單線程
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print("Total time (single thread): {}".format(end_time - start_time))

    # 同時執行的兩個並發線程, not that fast
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_array[tid] = t

    for i in range(2):
        thread_array[i].join()

    end_time = time.time()
    print("Total time (multi-thread): {}".format(end_time - start_time))

    '''

    # 在 window 中，像 PyInstaller 為了產生執行檔
    # multiprocessing 會被禁止，導致無法執行，出現 RuntimeError
    # 需在 start 前加入此 function，只在 window 有效，其餘無作用
    # 且在 __name__ == '__main__' 之後
    # freeze_support()
    # 指定產生 process 的方式，讓不同平台的表現一致
    # set_start_method('spawn')
    lock = Lock()
    qq = mpQ()
    for num in range(5):
        # 建立 child process
        p = Process(target=f, args=(qq, lock, num))
        # 開始執行 child process
        p.start()
        # blocking parent process 直到 child process 返回
        # 等待 0.1s，可為無參數，則表示永久等待
        p.join(timeout=0.1)


    while not qq.empty():
        print("show result ",qq.get())

    '''
    # multi-process with pool, not queue needed
    print('Parent process {}.'.format(os.getpid()))
    # 指定建立 child process 的數量，若無指定，預設為 cpu 數量
    multi_res = []
    with Pool(processes=3) as p:
        for i in range(5):
            # 建立 child process 並執行，error_callback 必須指定，不然很難 debug
            multi_res.append(p.apply_async(
                long_time_task, args=(i,), error_callback=handle_error))
        print('wait for all child processes finished')
        # 關掉 pool 不再加入任何 child process
        p.close()
        # 調用 join() 之前必須先調用close()
        p.join()

    print('all child processes completed. show return values',
          [res.get() for res in multi_res])

    print('share memory between processes')
    multicore()
