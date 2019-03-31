'''
using different class to represent the "states"

主要精神：以類別來表示狀態，切換類別表現 "狀態變化"

若狀態增多時，流程會變得冗長
如果狀態變化非線性結構(可能有個方向的狀態變化)時，
  結構化的設計方式，會造成程式碼閱讀、管理的麻煩。
'''

class State(object):
    def scan(self):
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(u"Scanning... Station is %s %s" % (self.stations[self.pos], self.name))


class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print(u"Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print(u"Switching to AM")
        self.radio.state = self.radio.amstate


class Radio(object):
    def __init__(self):
        """We have an AM state and an FM state"""
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


# Test our radio out
def main():
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    actions *= 2

    for action in actions:
        action()


if __name__ == '__main__':
    main()



import time

class Red:
    def change(self, light):
        print("紅燈")
        time.sleep(2)
        light.set(Green())

class Green:
    def change(self, light):
        print("綠燈")
        time.sleep(2)
        light.set(Yellow())

class Yellow:
    def change(self, light):
        print("黃燈")
        time.sleep(1)
        light.set(Red())

class TrafficLight:
    def __init__(self):
        self.current = Red()
    
    def set(self, state):
        self.current = state
    
    def change(self):
        self.current.change(self)
        
trafficLight = TrafficLight()
while True:
    trafficLight.change()

