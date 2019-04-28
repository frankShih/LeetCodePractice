'''
Provides an interface to resource that is expensive to duplicate.
(or time-consuming)

主要精神：通過引入代理對象，間接訪問目標對象

為物件提供一種代理，以控制對這個物件的訪問，根據的目不同，
代理物件將有不同責任，因而產生多種不同的代理情況。
e.g. preOperation, postOperation, 日誌， 甚至作為攔截器

silimar to facade, but proxy focus on "object" 
and control the accesibility of the "object"; 
on the other hand, facade focus on isolate a bunch of code,
and make the code clean and clear
'''



class RealSubject(object):
    def request(self):
        print('do something real')


class SubjectProxy(object):
    sub = None

    def request(self):
        if not self.sub:
            print('set up RealSubject')

            self.sub = RealSubject()
        
        print('do some pre-operation')
        self.sub.request()
        print('do some post-operation')


sp = SubjectProxy()
sp.request()

print('===================================')

import time


class SalesManager:
    def talk(self):
        print("Sales Manager ready to talk")


class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def talk(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(0.1)
            self.sales.talk()
        else:
            time.sleep(0.1)
            print("Sales Manager is busy")


class NoTalkProxy(Proxy):
    def talk(self):
        print("Proxy checking for Sales Manager availability")
        time.sleep(0.1)
        print("This Sales Manager will not talk to you", "whether he/she is busy or not")


if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()