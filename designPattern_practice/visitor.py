'''
Separates an algorithm (business logic) from an object structure

主要精神： 將繁瑣的物件類別判斷/操作，抽出來由 "額外的物件" 獨立管理

假設要對所有元素進行一項'處理'。常理判斷，應該寫在資料結構的類別裡，
不過如果這項'處理'的動作不只一個，每次做新處理時，就必須修改資料結構的類別。
=> 寫個在資料結構內來去的 visitor ，把處理交給 visitor 進行。
如此，想追加新的動作時，再建立新的 visitor 即可。
資料結構這邊，要能接受來敲門的訪客。(Acceptor 必須公開足夠的資訊給 Visitor)
(replace "if else" statement, make object structure more 'clean')


The Open-Closed Principle
    擴充(extension)時要開放(open)
    修改(modification)時要封閉(closed)

在設計類別時都應該容許以後繼續擴充該程式。這就是擴充時要開放。
如果每次擴充程式時還要去修改現有類別，那就太麻煩。
在擴充程式時沒有修改現有類別的需要正是"修改時要關閉"。
'''

class Customer:
    def doCustomer(self):
        print("customer services:")
    
    def pay(self):
        print("checkout")
    
    def accept(self, visitor): pass

class Member(Customer):
    def doMember(self):
        print("member services ~~")
    
    # accept 方法的呼叫為: acceptor.accept(visitor)
    def accept(self, visitor):
        visitor.visitMember(self)
    
class VIP(Customer):
    def doVIP(self):
        print("VIP services !!!")
        
    def accept(self, visitor):
        visitor.visitVIP(self)

class VisitorImpl:
    # visit 方法的呼叫為: visitor.visit(acceptor)
    def visitMember(self, member):
        member.doMember()
    
    def visitVIP(self, vip):
        vip.doVIP()
    
class Service:
    def __init__(self):
        self.visitor = VisitorImpl()
    
    def doService(self, customer):
        customer.doCustomer()
        customer.accept(self.visitor)
        customer.pay()

service = Service()
service.doService(VIP())
print("------------------")
service.doService(Member())
print("------------------")
service.doService(Customer())
print("------------------")
print([x for x in VIP.mro()])
print('=====================================')


class Node(object):
    pass

class A(Node):
    pass

class B(Node):
    pass

class C(A, B):
    pass

class Visitor(object):
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth_name = 'visit_' + cls.__name__
            meth = getattr(self, meth_name, None)
            if meth:
                break

        meth = meth if meth else self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print('generic_visit ' + node.__class__.__name__)

    def visit_B(self, node, *args, **kwargs):
        print('visit_B ' + node.__class__.__name__)


def main():
    a = A()
    b = B()
    c = C()
    visitor = Visitor()
    visitor.visit(a)
    visitor.visit(b)
    visitor.visit(c)


if __name__ == "__main__":
    main()






