'''
Decouples an abstraction from its implementation.
(very similar to visitor pattern)

主要精神：將抽象與實現分離，使兩者都可以獨立地"演化"
            抽象，是指應用程式行為定義的演化，
            實現，指的是應用程式實作時，所使用的 API 或平台

Bridge Pattern 居間溝通的兩個位置:
功能的類別階層 (Abstraction 的實作，不應該依賴於特定 API 或平台)
    基本功能放在父類別
    新功能則新增到子類別
實作的類別階層 (透過 Implementor 來橋接特定 API 或平台實現)
    父類別使用抽象方法來規定介面
    子類別使用具體方法來實作此介面

PS. bridge 對"一系列"的方法抽換包裝成 class 供外部使用；
    visitor 針對單一功能(方法)，對不同客戶端有不同實作，但統一抽出做管理
'''

# ======== implementation =========
class DrawingAPI(object):
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):  # ConcreteImplementor 1/2
    def draw_circle(self, x, y, radius):
        super().draw_circle(x, y, radius)
        print('API1.circle at {}:{} radius, {}'.format(x, y, radius))

class DrawingAPI2(DrawingAPI):  # ConcreteImplementor 2/2
    def draw_circle(self, x, y, radius):
        super().draw_circle(x, y, radius)

        print('API2.circle at {}:{} radius, {}'.format(x, y, radius))


# ========= Abstraction ==========
class CircleShape(object):
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    # low-level i.e. Implementation specific
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    # high-level i.e. Abstraction specific
    def scale(self, pct):
        self._radius *= pct


def main():
    shapes = (
                CircleShape(1, 2, 3, DrawingAPI1()), 
                CircleShape(5, 7, 11, DrawingAPI2())
            )

    for shape in shapes:
        shape.scale(2.5)
        shape.draw()


if __name__ == '__main__':
    main()
