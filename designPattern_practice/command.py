'''
Encapsulates information needed to perform actions / trigger events

主要精神：將指令的建立與執行分離
            事先無法預測或不想規範指令執行器的客戶端之指令內容。
            隔離（客戶端）建立指令時必須的參數（物件）。
            隔離（執行器端）執行指令物件時必要的資源。
            ...

將事件/指令變成物件，按照順序排入queue，再依序處理排列等候的事件。
指令執行器的 實現方式不是重點，只要能夠建立/執行指令即可

something like 'argParser' in python
'''


class Drawing:
    def processSome(self):
        print("    - 對圖片作 Some 處理")

    def processOther(self):
        print("    - 對圖片作 Other 處理")

    def processAnother(self):
        print("    - 對圖片作 Another 處理")


class ImageService:
    def __init__(self):
        self.commands = {}
        self.drawing = Drawing()

    def addCommand(self, effect, command):
        self.commands[effect] = command

    def doEffect(self, effect):
        self.commands[effect].execute(self.drawing)


class AEffectCommand:
    def execute(self, drawing):
        print("作 A 特效")
        drawing.processSome()
        drawing.processOther()


class BEffectCommand:
    def execute(self, drawing):
        print("作 B 特效")
        drawing.processOther()
        drawing.processAnother()


class CEffectCommand:
    def execute(self, drawing):
        print("作 C 特效")
        drawing.processOther()
        drawing.processSome()
        drawing.processAnother()


service = ImageService()
service.addCommand("AEffect", AEffectCommand())
service.addCommand("BEffect", BEffectCommand())
service.addCommand("CEffect", CEffectCommand())

service.doEffect("AEffect")
service.doEffect("BEffect")
service.doEffect("CEffect")

print("==========================================")


import os
from os.path import lexists


class MoveFileCommand(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self.rename(self.src, self.dest)

    def undo(self):
        self.rename(self.dest, self.src)

    def rename(self, src, dest):
        print(u"renaming %s to %s" % (src, dest))
        os.rename(src, dest)


def main():
    command_stack = []
    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))

    # verify that none of the target files exist
    assert not lexists("foo.txt")
    assert not lexists("bar.txt")
    assert not lexists("baz.txt")

    try:
        with open("foo.txt", "w"):  # Creating the file
            pass

        for cmd in command_stack:   
            cmd.execute()

        for cmd in reversed(command_stack):  # can be undone at will
            cmd.undo()
    finally:
        os.unlink("foo.txt")    # delete the testing file


if __name__ == "__main__":
    main()