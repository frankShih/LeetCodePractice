'''
Maintains a list of dependents and notifies them of any state changes.

主要精神：統一管理 registeration & notification

寫一些跟狀態變化有關的處理時，Observer Pattern 很好用
重點在 Observer Interface 以及具體實作的Observer類別。另外，也需要設計被觀察者。
observer, concrete observer, Subject, ConcreteSubject (被觀察者)
'''

# 被觀察者keep 所有觀察(訂閱)者的資訊，但不知道訂閱者是誰
class Subject(object):
    def __init__(self):
        self._observers = []

    def attach(self, obs):
        if obs not in self._observers:
            self._observers.append(obs)

    def detach(self, obs):
        try:
            self._observers.remove(obs)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # for obs in self._observers:
        #     if modifier != obs:
        #         obs.update(self)
        pass

class NewsStation(Subject):
    def __init__(self, naming=''):
        super().__init__()
        self._naming = naming   # underline -> private property

    @property
    def naming(self):
        return self._naming

    @naming.setter
    def naming(self, val):  #the assignment call setter automatically
        self._naming = val
        print("name is changing~~")
        # do some checking here
        self.sendNews("the station change name to: {}".format(self.naming))
        return self._naming

    def subcribeNews(self, obs):
        super().attach(obs)
        print("new subscriber !!!")

    def unsubcribeNews(self, obs):
        super().detach(obs)
        print("bye bye ~ subscriber ...")

    def sendNews(self, content):
        for o in self._observers:
            o.update(content)   # send string

# observer, waiting for notification passively
class Observer(object):
    def update(self):
        pass


class Customer(Observer):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def update(self, msg):
        print("customer - {} received a message: {}".format(self.name, msg))



if __name__ == "__main__":
    c1 = Customer("alice")
    c2 = Customer("bob")

    ns = NewsStation("ABC")
    ns.attach(c1)
    ns.attach(c2)

    print(ns.naming)
    ns.naming = "BBC"
    print(ns.naming)

