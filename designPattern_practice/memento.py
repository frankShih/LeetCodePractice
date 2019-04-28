from copy import deepcopy
from copy import copy
'''
Provides the ability to restore an object to its previous state.

主要精神：獨立於 object 外的備份還原功能

使用 Backup 物件封裝想備份的資訊，Application 負責建立 Backup 物件，
建立的 Backup 物件則交由 Recovery 物件管理
'''

import time


class Backup:
    def __init__(self, state):
        self.state = state
        self.date = time.ctime()


class Application:
    def __init__(self):
        self.state = "default setting"

    def backup(self):
        return Backup(self.state)

    def recover(self, backup):
        self.state = backup.state


class Recovery:
    def __init__(self):
        self.backups = []

    def add(self, backup):
        self.backups.append(backup)

    def retrieve(self, date):
        for backup in self.backups:
            if backup.date == date:
                self.backups.remove(backup)
                return backup
        return None


application = Application()
recovery = Recovery()

print(application.state)

backup = application.backup()  # 建立備忘
recovery.add(backup)  # 加入備忘錄

application.state = "customer setting"
print(application.state)

date = backup.date  # 假設 date 是使用者自行設定所要取得的還原時間！
application.recover(recovery.retrieve(date))  # 取得備忘來還原
print(application.state)


print("=====================================\n")


def memento(obj, deep=False):
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():  # closure, save context & return
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore  # return roll-back function

# perform rollback explicitly


class Transaction(object):
    """
    A transaction guard.
    just syntactic sugar around a memento closure.
    """

    deep = False
    states = []

    def __init__(self, deep, *targets):
        self.deep = deep
        self.targets = targets
        self.commit()

    def commit(self):
        self.states = [memento(target, self.deep) for target in self.targets]

    def rollback(self):
        for a_state in self.states:
            a_state()

# perform rollback implicitly


class Transactional(object):
    """
    Adds transactional semantics to methods. 
    Methods decorated with @Transactional will 
    rollback to entry-state upon exceptions.
    """

    def __init__(self, method):
        self.method = method

    '''
    當物件擁有 __get__（必要），以及 __set__、__delete__ (選擇性)，
    它可以作為描述器（Descriptor）：
        def __get__(self, instance, owner)
        def __set__(self, instance, value)
        def __delete__(self, instance)
    
    如果執行：
        s = Some()
        s.x
        s.x = 10
        del s.x

        其實相當於這麼作：
        s = Some()
        Some.__dict__['x'].__get__(s,  Some);
        Some.__dict__['x'].__set__(s,  10);
        Some.__dict__['x'].__delete__(s);
    '''

    def __get__(self, obj, T):
        def transaction(*args, **kwargs):
            state = memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e

        return transaction


class NumObj(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.value)

    def increment(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = '1111'  # <- invalid value
        self.increment()  # <- will fail and rollback


def main():
    """
    >>> num_obj = NumObj(-1)
    >>> print(num_obj)
    <NumObj: -1>
    >>> a_transaction = Transaction(True, num_obj)
    >>> try:
    ...    for i in range(3):
    ...        num_obj.increment()
    ...        print(num_obj)
    ...    a_transaction.commit()
    ...    print('-- committed')
    ...    for i in range(3):
    ...        num_obj.increment()
    ...        print(num_obj)
    ...    num_obj.value += 'x'  # will fail
    ...    print(num_obj)
    ... except Exception:
    ...    a_transaction.rollback()
    ...    print('-- rolled back')
    <NumObj: 0>
    <NumObj: 1>
    <NumObj: 2>
    -- committed
    <NumObj: 3>
    <NumObj: 4>
    <NumObj: 5>
    -- rolled back
    >>> print(num_obj)
    <NumObj: 2>
    >>> print('-- now doing stuff ...')
    -- now doing stuff ...
    >>> try:
    ...    num_obj.do_stuff()
    ... except Exception:
    ...    print('-> doing stuff failed!')
    ...    import sys
    ...    import traceback
    ...    traceback.print_exc(file=sys.stdout)
    -> doing stuff failed!
    Traceback (most recent call last):
    ...
    TypeError: ...str...int...
    >>> print(num_obj)
    <NumObj: 2>
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS, verbose=True)
