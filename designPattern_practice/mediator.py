'''
Encapsulates how a set of objects interact.

主要精神：中介的物件來封裝物件之間的交互

物件間並不用互相知道另一方，這可降低物件之間的耦合性，
要改變物件間的交互行為，只需要對 Mediator 加以修改即可。
'''


class ChatRoom(object): # share information via mediator
    """Mediator class"""

    def display_message(self, user, message):
        print("[{} says]: {}".format(user, message))


class User(object):
    """A class whose instances want to interact with each other"""

    def __init__(self, name):
        self.name = name
        self.chat_room = ChatRoom()

    def say(self, message):
        self.chat_room.display_message(self, message)

    def __str__(self):
        return self.name


def main():
    molly = User('Molly')
    mark = User('Mark')
    ethan = User('Ethan')

    molly.say("Hi Team! Meeting at 3 PM today.")
    mark.say("Roger that!")
    ethan.say("Alright.")


if __name__ == '__main__':
    main()
