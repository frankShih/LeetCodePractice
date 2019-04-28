'''
Describes a group of objects that is treated as a single instance.

主要精神：對容器和內容一視同仁，把複數物體集中在一起，像是處理一個整體。

具層次/組合性的物件可使用 Composite pattern，像電路、視窗元件等，
使用 Composite pattern 大大減低這些元件設計的複雜度

舉例來說，目錄和檔案都可以放在目錄底下，因此可以一視同仁。
File、Directory 類別，兩者合併父類別 Entry。
Entry 類別是表示目錄進入點的類別，對 File 和 Directory 一視同仁的類別。

'''

class Frame:
    def __init__(self, image):
        self.image = image
    def play(self):
        print("播放 " + self.image)

class Playlist:
    def __init__(self):
        self.list = []
    def add(self, playable):
        self.list.append(playable);
    def play(self):
        for playable in self.list:
            playable.play()
            
logo = Frame("start of file: LOGO")
        
playlist1 = Playlist()
playlist1.add(Frame("actor wave left hand"))
playlist1.add(Frame("actor wave right hand"))
        
playlist2 = Playlist()
playlist2.add(Frame("actor shake left foot"))
playlist2.add(Frame("actor shake right foot"))
        
all = Playlist()
all.add(logo)
all.add(playlist1)
all.add(playlist2)

all.play()

print('=====================================')

class Graphic:
    def render(self):
        raise NotImplementedError("You should implement this.")


class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def render(self):
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name):
        self.name = name

    def render(self):
        print("Ellipse: {}".format(self.name))


if __name__ == '__main__':
    ellipse1 = Ellipse("1")
    ellipse2 = Ellipse("2")
    ellipse3 = Ellipse("3")
    ellipse4 = Ellipse("4")

    graphic1 = CompositeGraphic()
    graphic2 = CompositeGraphic()

    graphic1.add(ellipse1)
    graphic1.add(ellipse2)
    graphic1.add(ellipse3)
    graphic2.add(ellipse4)

    graphic = CompositeGraphic()

    graphic.add(graphic1)
    graphic.add(graphic2)

    graphic.render()