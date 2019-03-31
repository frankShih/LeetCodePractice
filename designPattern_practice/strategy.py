'''
define a group of method (strategy), and user can change it in runtime.

主要精神： 提供可自行切換之接口

解決問題時需要實作一些特定的運算法則。
在 Strategy Pattern 之下，可以更換實作運算法則的部份而且不留痕跡。
'''
import enum
import random


class Hands(enum.Enum):
    Paper = 0
    Scissor = 1
    Stone = 2

def StrategyRandom(lastResult=None):
    return random.choice(list(Hands))

def StrategyNotLose(lastResult):
    print(lastResult)
    if lastResult[0]==None:   # first play
        return StrategyRandom()
    elif lastResult[0]<0: #lose
        return random.choice([x for x in list(Hands) if x != lastResult[1]])
    else:   # tie /win
        return lastResult[1]

class Player(object):
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.winCount = 0
        self.loseCount = 0
        self.tieCount = 0
        self.lastResult = [None, None]  # compare result, hand

    def showHand(self):
        return self.strategy(self.lastResult)

    def setRecord(self, res, resHand):
        self.lastResult = [res, resHand]
        if res>0:
            self.winCount+=1
        elif not res:
            self.tieCount+=1
        else:
            self.loseCount+=1




class PaperScissorStone_game(object):
    # paper=0, scissor=1, stone=2

    def __init__(self, player1, player2):
        self.p1 =  player1
        self.p2 =  player2

    def judge(self):
        p1Result, p2Result = self.p1.showHand(), self.p2.showHand()
        outcome = None
        if p1Result==p2Result:
            self.p1.setRecord(0, p1Result)
            self.p2.setRecord(0, p2Result)
            outcome = 'tie'
        elif p1Result ==Hands.Paper and p2Result==Hands.Scissor or\
           p1Result ==Hands.Scissor and p2Result==Hands.Stone or\
           p1Result ==Hands.Stone and p2Result==Hands.Paper:
            self.p1.setRecord(-1, p1Result)
            self.p2.setRecord(1, p2Result)
            outcome='player2 win'
        else:
            self.p1.setRecord(1, p1Result)
            self.p2.setRecord(-1, p2Result)
            outcome='player1 win'

        print("{}: {}, {}: {}. outcome: {}.".format(self.p1.name, p1Result, self.p2.name, p2Result, outcome))

if __name__ == "__main__":
    p1 = Player("alice", StrategyRandom)
    p2 = Player("bob", StrategyNotLose)

    game = PaperScissorStone_game(p1, p2)
    game.judge()
    game.judge()
    game.judge()
    game.judge()
    game.judge()
